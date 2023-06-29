import tiledb
import cv2
import numpy as np
import time
import av
import io
import os
import tiledb
import numpy as np
import time
import os

TILE_DB_PATH = os.environ["TILE_DB_PATH"]
SAMPLE_VIDEO_PATH = os.environ["SAMPLE_VIDEO_PATH"]

def save_video_to_tiledb(video_path, tiledb_uri):
    # Open the video file
    container = av.open(video_path)
    video = container.streams.video[0]
    num_frames = video.frames
    frame_width = video.codec_context.format.width
    frame_height = video.codec_context.format.height

    # Create a TileDB array context
    ctx = tiledb.Ctx()

    schema = tiledb.ArraySchema( 
        domain=tiledb.Domain(
            tiledb.Dim(ctx=ctx, domain=(0, num_frames-1), tile=1, dtype=np.uint32),
            tiledb.Dim(ctx=ctx, domain=(0, frame_height-1), tile=frame_height, dtype=np.uint32),
            tiledb.Dim(ctx=ctx, domain=(0, frame_width-1), tile=frame_width, dtype=np.uint32),
            tiledb.Dim(ctx=ctx, domain=(0, 2), tile=3, dtype=np.uint32),
            ctx=ctx
        ),
        attrs=[tiledb.Attr(name="bgr", dtype=np.uint8, ctx=ctx)],
        ctx=ctx,
        sparse=False
    )

    frames = []
    for frame in container.decode(video=0):
        # Convert the frame to a NumPy array
        frame_np_array = frame.to_ndarray(format='bgr24')
        frames.append(frame_np_array)
    
    if tiledb.object_type(tiledb_uri, ctx) != "array":
        # Create the TileDB array
        tiledb.Array.create(tiledb_uri, schema)
    
    print("Number of frames: ", frames.__len__())
    start = time.time()
    # Open the TileDB array in write mode
    with tiledb.open(tiledb_uri, 'w') as arr:
        arr[:] = np.array(frames)
    end = time.time()
    print(f"Total time taken: ", abs(end-start))

# Usage example
video_path = SAMPLE_VIDEO_PATH
tiledb_uri = TILE_DB_PATH

save_video_to_tiledb(video_path, tiledb_uri)

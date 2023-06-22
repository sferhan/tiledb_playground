import tiledb
import numpy as np
import time
import os

TILE_DB_PATH = os.environ["TILE_DB_PATH"]
SAMPLE_VIDEO_PATH = os.environ["SAMPLE_VIDEO_PATH"]

def save_video_to_tiledb(video_path, tiledb_uri):
    # Open the video file
    video_file = open(video_path, 'rb')
    
    # Read the video content
    video_content = video_file.read()
    
    # Close the video file
    video_file.close()
    
    # Create a TileDB array context
    ctx = tiledb.Ctx()
    
    # Create a TileDB array schema
    schema = tiledb.ArraySchema( 
        domain=tiledb.Domain(
            tiledb.Dim(ctx=ctx, domain=(0, len(video_content)-1), tile=1, dtype=np.bytes_), ctx=ctx
        ),
        attrs=[tiledb.Attr(name="video", dtype=np.bytes_, ctx=ctx)],
        ctx=ctx,
        sparse=True
    )
    
    if tiledb.object_type(tiledb_uri, ctx) != "array":
        # Create the TileDB array
        tiledb.Array.create(tiledb_uri, schema)
    
    start = time.time()
    # Open the TileDB array in write mode
    with tiledb.open(tiledb_uri, 'w') as arr:
        arr[:] = video_content
    end = time.time()
    print(f"Total time taken: ", abs(end-start))

# Usage example
video_path = SAMPLE_VIDEO_PATH
tiledb_uri = TILE_DB_PATH

save_video_to_tiledb(video_path, tiledb_uri)
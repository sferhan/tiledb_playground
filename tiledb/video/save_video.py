import tiledb
import numpy as np
import time

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
    
    # Create the TileDB array
    tiledb.Array.create(tiledb_uri, schema)
    
    start = time.time()
    # Open the TileDB array in write mode
    with tiledb.open(tiledb_uri, 'w') as arr:
        arr[:] = video_content
    end = time.time()
    print(f"Total time taken: ", abs(end-start))

# Usage example
video_path = "/Users/ferhanhaider/Desktop/Workspaces/Study/research_project/playground/tiledb_playground/tiledb/video/sample-5s.mp4"
tiledb_uri = "/Users/ferhanhaider/Desktop/Workspaces/Study/research_project/playground/tiledb_playground/tiledb/video/video.array"

save_video_to_tiledb(video_path, tiledb_uri)
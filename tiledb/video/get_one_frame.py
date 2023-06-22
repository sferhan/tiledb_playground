import tiledb
import cv2
import numpy as np
import time
import av
import io
import os

TILE_DB_PATH = os.environ["TILE_DB_PATH"]

ctx = tiledb.Ctx()
array_uri = TILE_DB_PATH

desired_frame = None

start = time.time()

with tiledb.SparseArray(array_uri) as array:
    video_stream = io.BytesIO(array[:]["video"][0])
    video = av.open(video_stream)
    frame_index = 100
    video.seek(frame_index)
    for frame in video.decode(video=0):
        if frame.index == frame_index:
            desired_frame = frame.to_ndarray(format='bgr24')
    video.close()

end = time.time()
print(f"Total time taken for retrieving one frame from video is : {abs(end-start)} seconds")

cv2.imshow("Frame", desired_frame)
# Wait for key press to exit
cv2.waitKey(0)

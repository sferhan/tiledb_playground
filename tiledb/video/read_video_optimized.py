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

frames = []

with tiledb.DenseArray(array_uri) as array:
    frames = array[:, :, :, :]['bgr']

end = time.time()
print(f"Total time taken for retrieving one frame from video is : {abs(end-start)} seconds")

for frame in frames:
    f = av.VideoFrame.from_ndarray(frame, format='bgr24')
    cv2.imshow("Frame", f.to_ndarray(format='bgr24'))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Wait for key press to exit
cv2.waitKey(0)

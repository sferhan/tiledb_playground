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

with tiledb.DenseArray(array_uri) as array:
    frame = av.VideoFrame.from_ndarray(array[80:81, :, :, :]['bgr'][0], format='bgr24')

end = time.time()
print(f"Total time taken for retrieving one frame from video is : {abs(end-start)} seconds")

cv2.imshow("Frame", frame.to_ndarray(format='bgr24'))
# Wait for key press to exit
cv2.waitKey(0)

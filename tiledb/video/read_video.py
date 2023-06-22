import tiledb
import cv2
import numpy as np
import time
import av
import io

ctx = tiledb.Ctx()
array_uri = "./tiledb/video/video.array"

frames = []
start = time.time()
with tiledb.SparseArray(array_uri) as array:

    start1 = time.time()
    video_stream = io.BytesIO(array[:]["video"][0])
    end1 = time.time()
    print(f"T1 : {abs(end1-start1)} seconds")

    video = av.open(video_stream)

    start2 = time.time()
    for frame in video.decode(video=0):
        # Convert the frame to a NumPy array
        frame_np_array = frame.to_ndarray(format='bgr24')

        frames.append(frame_np_array)
    end2 = time.time()
    print(f"T2 : {abs(end2-start2)} seconds")
    video.close()

end = time.time()
print(f"Total time taken for reading the complete video is : {abs(end-start)} seconds")

for frame in frames:
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

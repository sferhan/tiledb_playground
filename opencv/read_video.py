import cv2
import time
import os

SAMPLE_VIDEO_PATH = os.environ["SAMPLE_VIDEO_PATH"]

frames  = []

start = time.time()

video_source = cv2.VideoCapture(SAMPLE_VIDEO_PATH)
while video_source.isOpened():
    ret, frame = video_source.read()
    if not ret:
        break    
    frames.append(frame)

end = time.time()
print(f"Total time taken for reading the complete video is : {abs(end-start)} seconds")

for frame in frames:
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_source.release()
cv2.destroyAllWindows()

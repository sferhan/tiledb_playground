import cv2
import time

frames  = []

start = time.time()

video_source = cv2.VideoCapture('./sample-5s.mp4')
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

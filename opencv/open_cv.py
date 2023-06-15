import cv2
import time

video_source = cv2.VideoCapture('./sample-5s.mp4')

output_filename = 'output.mp4'

fourcc = int(video_source.get(cv2.CAP_PROP_FOURCC))
codec = chr(fourcc&0xff) + chr((fourcc>>8)&0xff) + chr((fourcc>>16)&0xff) + chr((fourcc>>24)&0xff)

fps = int(video_source.get(cv2.CAP_PROP_FPS))
frame_w, frame_h = int(video_source.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video_source.get(cv2.CAP_PROP_FRAME_HEIGHT))
video_writer = cv2.VideoWriter(output_filename, fourcc, fps, (frame_w, frame_h))

frames = []
while video_source.isOpened():
    ret, frame = video_source.read()
    if not ret:
        break
    frames.append(frame)

start = time.time()
for f in frames:
    video_writer.write(f)
end = time.time()

print(f"Total time taken for fourcc: '{codec}' is : ", abs(end-start))

video_source.release()
video_writer.release()
cv2.destroyAllWindows()

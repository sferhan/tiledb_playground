import cv2
import time

# Open the video file
video_path = './sample-5s.mp4'

start = time.time()
cap = cv2.VideoCapture(video_path)

# Check if the video file was opened successfully
if not cap.isOpened():
    print("Error opening video file")
    exit()

# Set the desired frame position (index of the frame you want)
frame_index = 100  # Change this to the desired frame index

# Set the frame position in the video
cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)

# Read the frame at the specified position
ret, frame = cap.read()

end = time.time()
print(f"Total time taken for retrieving one frame from video is : {abs(end-start)} seconds")

# Check if the frame was read successfully
if not ret:
    print("Error reading frame")
    exit()

# Display the retrieved frame
cv2.imshow("Frame", frame)

# Wait for key press to exit
cv2.waitKey(0)

# Release the video file and close any open windows
cap.release()
cv2.destroyAllWindows()
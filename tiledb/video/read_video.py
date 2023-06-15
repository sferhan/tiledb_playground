import tiledb
import cv2
import numpy as np
import tempfile
import av

ctx = tiledb.Ctx()
array_uri = "/Users/ferhanhaider/Desktop/Workspaces/Study/research_project/playground/tiledb_playground/tiledb/video/video.array"
with tiledb.SparseArray(array_uri) as array:
    schema = array.schema

    video_stream = array[:]["video"][0]
    print("Length of video saved to TileDB: ", len(array[:]["video"][0]))
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(video_stream)
    temp_file.close()

    video_source = cv2.VideoCapture(temp_file.name)
    if not video_source.isOpened():
        print("Error opening video")
        exit()
    else:
        frames = []
        while video_source.isOpened():
            ret, frame = video_source.read()
            if not ret:
                break
            cv2.imshow("Frame", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    video_source.release()
    cv2.destroyAllWindows()

    # frame_shape = attrs["video"].shape
    # frame_dtype = attrs["video"].dtype

    # with array.query(attrs=["video"]) as q:
    #     q.add_range(
    #         dim=0,
    #         start=0,  # Start frame index
    #         end=frame_shape[0]  # End frame index
    #     )
    #     q.submit()
    #     frames = q.results()["frames"]
        
    #     for frame in frames:
    #         # Convert the frame data to the appropriate format for OpenCV
    #         frame_data = np.frombuffer(frame, dtype=frame_dtype).reshape(frame_shape[1:])
    #         frame_data = cv2.cvtColor(frame_data, cv2.COLOR_BGR2RGB)  # If needed, convert color space
            
    #         # Process the frame (e.g., display, save, etc.)
    #         cv2.imshow("Video", frame_data)
    #         if cv2.waitKey(1) & 0xFF == ord('q'):
    #             break

## Summary
Just playing around with TileDB and OpenCV with the following goals
1. Understand how to use TileDB
2. Figure out different ways to save images and videos in TileDB
3. Understand video concepts - formats, codecs, compression etc.
4. Perform Read/Write operations on images & videos using TileDB and OpenCV video-writer and compare their performance

## Setting Up
Setup Python environment
```
python3 -m venv venv
source ./venv/bin/activate
pip install -r ./requirements.txt
```
Export environment variables
```
export OUTPUT_VIDEO_PATH=./output.mp4
export TILE_DB_PATH=./tiledb/video/video.array
export SAMPLE_VIDEO_PATH=./sample-5m43s.mp4
```

## Operations
Execute from the root of the repository

### Read Complete Video
#### OpenCV
```
python3 ./opencv/read_video.py
```
#### TileDB
```
python3 ./tiledb/video/read_video.py
```

### Save Complete Video
#### OpenCV
```
python3 ./opencv/save_video.py
```
#### TileDB
```
python3 ./tiledb/video/save_video.py 
```

### Read One Frame
#### OpenCV
```
python3 ./opencv/get_one_frame.py
```
#### TileDB
```
python3 ./tiledb/video/get_one_frame.py 
```
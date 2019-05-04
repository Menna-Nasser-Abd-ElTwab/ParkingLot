import yaml
import cv2
from modules.config import *
from modules.init_parking import init_parking

parking_bounding_rects = []

# Read YAML data (parking space polygons)
with open(fn_yaml, 'r') as stream:
    parking_data = yaml.load(stream)

# Init parking data
init_parking(parking_data, parking_bounding_rects)

# during app is running
while(cap.isOpened()):

    # Read frame-by-frame
    video_cur_pos = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000.0 # Current position of the video file in sec
    vv_current_frame = cap.get(cv2.CAP_PROP_POS_FRAMES) # Index of frame to be captured at the next
    ret, frame = cap.read()

cap.release()
cv2.destroyAllWindows()
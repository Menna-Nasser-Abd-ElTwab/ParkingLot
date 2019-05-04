import yaml
import cv2
from modules.config import *
from modules.init_parking import init_parking
from modules.init_parking_data import *
from modules.parking_detection import parking_detection

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

    if ret == False:
        print("There is error in capture, Please try again")
        break

    # Background Subtraction
    f_bluring = cv2.GaussianBlur(frame.copy(), (5,5), 3)
    f_gray = cv2.cvtColor(f_bluring, cv2.COLOR_BGR2GRAY)
    f_out = frame.copy()

    # Detect parking (Background Subtraction)
    parking_detection(parking_bounding_rects, f_gray, parking_lot_state, parking_buffer, video_cur_pos, parking_data)

cap.release()
cv2.destroyAllWindows()







import yaml
import cv2

fn = "datasets/parking1.mp4"
fn_yaml = "datasets/parking1.yml"
fn_out = "datasets/output.avi"


# Read YAML data (parking space polygons)
with open(fn_yaml, 'r') as stream:
    parking_data = yaml.load(stream)

# during app is running
while(cap.isOpened()):

    # Read frame-by-frame
    video_cur_pos = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000.0 # Current position of the video file in sec
    vv_current_frame = cap.get(cv2.CAP_PROP_POS_FRAMES) # Index of frame to be captured at the next
    ret, frame = cap.read()

cap.release()
cv2.destroyAllWindows()
import numpy as np
import cv2

# Init parking data
def init_parking(parking_data, parking_bounding_rects):
	for park in parking_data:
	    coors = np.array(park['coors'])
	    rect = cv2.boundingRect(coors)
	    parking_bounding_rects.append(rect)
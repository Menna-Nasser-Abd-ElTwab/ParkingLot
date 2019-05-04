import cv2

def keyboard_options(vv_current_frame, f_out):
  k = cv2.waitKey(1)

  if k == ord('c'):
    cv2.imwrite('export_frames/frame-%d.jpg' % vv_current_frame, f_out)
  elif k == ord('j'):
    cap.set(cv2.CAP_PROP_POS_FRAMES, vv_current_frame + 1000) # jump to frame
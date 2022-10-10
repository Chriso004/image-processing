import cv2
from Common.utils import *

capture = cv2.VideoCapture(0)

if capture.isOpened() is False:
    raise Exception("카메라 연결 안됨")

camera_set = utils.CameraSet()

while True:
    ret, frame = capture.read()
    if not ret: break

    key = cv2.waitKeyEx(1)
    if key == 27: break
    else: key_input(key, camera_set)

    frame = get_filtered_image(frame, camera_set)
    frame = get_divided_image(frame, camera_set)

    cv2.imshow("camera", frame)
capture.release()

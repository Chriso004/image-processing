import cv2
import numpy as np
import sys
from final_project.Common import utils


def bgr_to_gray(image):
    dst = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return dst


def complementary_image(image):
    hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv_img)
    temp = (h + 90) % 181
    h = np.array(temp, np.uint8)
    c_hsv = cv2.merge((h, s, v))
    dst = cv2.cvtColor(c_hsv, cv2.COLOR_HSV2BGR)

    return dst


def canny_detection(image):
    dst = cv2.Canny(image, 50, 80)
    return dst


def rev_canny_detection(image):
    canny = cv2.Canny(image, 10, 100)
    dst = np.zeros_like(canny)
    dst[canny==0] = 255
    dst[canny==255] = 0
    return dst


def image_to_pixel(image):
    # dst_size = (int(dst.shape[0] * 0.05), int(dst.shape[1] * 0.05), 3)
    # dst = scaling(image, size)
    dst_size = (int(image.shape[1] * 0.05), int(image.shape[0] * 0.05))
    dst = cv2.resize(image, dst_size, interpolation=cv2.INTER_LINEAR)
    # img_size = (int(image.shape[0]), int(image.shape[1]), 3)
    # pixel = scaling(image, size)
    img_size = (image.shape[1], image.shape[0])
    pixel = cv2.resize(dst, img_size, interpolation=cv2.INTER_LINEAR)
    return pixel


def afterimage(image):
    dst = np.array(image, np.uint8)

    if after.flag:
        temp = after.get_temp_image()
        dst = image * 0.15 + temp * 0.85
        dst = np.array(dst, np.uint8)
    after.set_temp_image(dst)

    return dst


def delay_screen(image, divide=9):
    dst = np.zeros_like(image, np.uint8)
    dx, dy = (int(image.shape[1] / 3), int(image.shape[0] / 3))
    divide_img = cv2.resize(image, (dx, dy), 0, 0, cv2.INTER_LINEAR)

    count = delay.get_count()
    delay_time = delay.get_delay()

    if count == sys.maxsize:
        delay.set_count(0)

    for i in range(divide):
        index = i * delay_time
        width = i % 3
        height = int(i / 3)
        delay.set_delay_image(divide_img, delay.count % (delay_time * divide))

        if count >= index:
            delay_img = delay.get_delay_image((count - index) % (delay_time * divide))
            dst[dy * height: dy * (height + 1), dx * width: dx * (width + 1)] = delay_img

    delay.increase_count()

    return dst


delay = utils.DelayScreen()
after = utils.AfterImage()

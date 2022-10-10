from final_project.Common.filter import *
from final_project.Common.mode import *
from enum import Enum


class Division(Enum):
    NORMAL = 1
    DIVISION_2 = 2
    REV_DIVISION_2 = 3
    DIVISION_3 = 4
    DIVISION_4 = 5
    REV_DIVISION_4 = 6
    DIVISION_9 = 7
    SIZE = 8


class Filter(Enum):
    NORMAL = 1
    GRAY = 2
    COMPLEMENTARY = 3
    CANNY = 4
    REVERSE_CANNY = 5
    PIXEL = 6
    AFTER = 7
    DELAY = 8
    SIZE = 9


class CameraSet:
    def __init__(self):
        self.div_mode = 1
        self.filter_mode = 1

    def set_div_mode(self, div_mode):
        self.div_mode = div_mode

    def set_filter_mode(self, filter_mode):
        self.filter_mode = filter_mode

    def get_div_mode(self):
        return self.div_mode

    def get_filter_mode(self):
        return self.filter_mode


class AfterImage:
    def __init__(self):
        self.temp_image = None
        self.flag = False

    def set_temp_image(self, image):
        self.temp_image = image
        self.flag = True

    def get_temp_image(self):
        return self.temp_image

    def get_flag(self):
        return self.flag


class DelayScreen:
    def __init__(self):
        self.count = 0
        self.delay_image = [None for i in range(90)]
        self.delay = 10

    def increase_count(self):
        self.count += 1

    def set_delay_image(self, image, i):
        self.delay_image[i] = image

    def set_count(self, count):
        self.count = count

    def set_delay(self, delay):
        self.delay = delay

    def get_delay_image(self, i):
        return self.delay_image[i]

    def get_count(self):
        return self.count

    def get_delay(self):
        return self.delay


def filter_previous(f_mode):
    if f_mode - 1 <= 0:
        return 1
    return f_mode - 1


def filter_next(f_mode):
    if f_mode + 1 >= Filter.SIZE.value:
        return f_mode
    return f_mode + 1


def division_previous(div_mode):
    if div_mode - 1 <= 0:
        return 1
    return div_mode - 1


def division_next(div_mode):
    if div_mode + 1 >= Division.SIZE.value:
        return div_mode
    return div_mode + 1


def key_input(key, camera_set):
    filter_mode = camera_set.get_filter_mode()
    div_mode = camera_set.get_div_mode()

    if key == 63232:
        camera_set.set_filter_mode(filter_next(filter_mode))
    if key == 63233:
        camera_set.set_filter_mode(filter_previous(filter_mode))
    if key == 63234:
        camera_set.set_div_mode(division_previous(div_mode))
    if key == 63235:
        camera_set.set_div_mode(division_next(div_mode))

    return div_mode, filter_mode


def get_filtered_image(image, camera_set):
    dst = np.array(image)
    filter_mode = camera_set.get_filter_mode()

    if filter_mode is Filter.GRAY.value:
        dst = bgr_to_gray(image)
    elif filter_mode is Filter.COMPLEMENTARY.value:
        dst = complementary_image(image)
    elif filter_mode is Filter.CANNY.value:
        dst = canny_detection(image)
    elif filter_mode is Filter.REVERSE_CANNY.value:
        dst = rev_canny_detection(image)
    elif filter_mode is Filter.PIXEL.value:
        dst = image_to_pixel(image)
    elif filter_mode is Filter.AFTER.value:
        dst = afterimage(image)
    elif filter_mode is Filter.DELAY.value:
        dst = delay_screen(image, 9)
    if filter_mode != Filter.DELAY.value and delay.get_count() != 0:
        delay.set_count(0)

    return dst


def get_divided_image(image, camera_set):
    dst = np.array(image)
    div_mode = camera_set.get_div_mode()

    if div_mode is Division.DIVISION_2.value:
        dst = division2(image)
    elif div_mode is Division.REV_DIVISION_2.value:
        dst = reverse_division2(image)
    elif div_mode is Division.DIVISION_3.value:
        dst = division3(image)
    elif div_mode is Division.DIVISION_4.value:
        dst = division4(image)
    elif div_mode is Division.REV_DIVISION_4.value:
        dst = reverse_division4(image)
    elif div_mode is Division.DIVISION_9.value:
        dst = division9(image)

    return dst

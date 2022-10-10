import numpy as np
import cv2


# def scaling(image, size):
#     dst = np.zeros(size, np.uint8)
#     ratio_y, ratio_x = image.shape[0] / size[0], image.shape[1] / size[1]
#     for y in range(image.shape[0]):
#         for x in range(image.shape[1]):
#             i, j = int(y / ratio_y), int(x / ratio_x)
#             dst[i, j, ::] = image[y, x, ::]
#
#     return dst


def division2(image):
    dst = np.zeros_like(image)
    # size = (int(dst.shape[0]), int(dst.shape[1] * 0.5), 3)
    # dst_2 = scaling(image, size)
    size = (int(dst.shape[1] * 0.5), int(dst.shape[0]))
    dst_2 = cv2.resize(image, size, 0, 0, cv2.INTER_LINEAR)

    dst = cv2.repeat(dst_2, 1, 2)

    # d2_size = dst_2.shape[1]
    # dst[:, :dst_2.shape[1]] = dst_2
    # dst[:, dst_2.shape[1]:image.shape[1]] = dst_2
    #
    return dst


def reverse_division2(image):
    dst = np.zeros_like(image)
    # size = (int(dst.shape[0]), int(dst.shape[1] * 0.5), 3)
    # dst_2 = scaling(image, size)
    size = (int(dst.shape[1] * 0.5), dst.shape[0])
    dst_2 = cv2.resize(image, size, 0, 0, cv2.INTER_LINEAR)

    d_size = dst_2.shape[1]
    dst[:, 0:d_size] = dst_2
    dst_2 = cv2.flip(dst_2, 1)
    dst[:, d_size:image.shape[1]] = dst_2

    return dst


def division3(image):
    dst = np.zeros_like(image)
    # size = (int(dst.shape[0]), int(dst.shape[1] * 0.333), 3)
    # dst_3 = scaling(image, size)
    size = (int(dst.shape[1] * 0.333), dst.shape[0])
    dst_3 = cv2.resize(image, size, 0, 0, cv2.INTER_LINEAR)

    dst = cv2.repeat(dst_3, 1, 3)
    # dst[:, :dst.shape[1] = dst_3
    # dst[:, dst.shape[1]:dst.shape[1]*2] = dst_3
    # dst[:, dst.shape[1] * 2:dst.shape[1] * 3] = dst_3

    return dst


def division4(image):
    dst = np.zeros_like(image)
    # size = (int(dst.shape[0] * 0.5), int(dst.shape[1] * 0.5), 3)
    # dst_4 = scaling(image, size)
    size = (int(dst.shape[1] * 0.5), int(dst.shape[0] * 0.5))
    dst_4 = cv2.resize(image, size, 0, 0, cv2.INTER_LINEAR)

    dst = cv2.repeat(dst_4, 2, 2)
    # dst[:dst_4.shape[0], :dst_4.shape[1]] = dst_4
    # dst[:dst_4.shape[0], dst_4.shape[1]:dst_4.shape[1] * 2] = dst_4
    # dst[dst_4.shape[0]:dst_4.shape[0] * 2, :dst_4.shape[1]] = dst_4
    # dst[dst_4.shape[0]:dst_4.shape[0] * 2, dst_4.shape[1]:dst_4.shape[1] * 2] = dst_4

    return dst


def reverse_division4(image):
    dst = np.zeros_like(image)
    # size = (int(dst.shape[0] * 0.5), int(dst.shape[1] * 0.5), 3)
    # dst_4 = scaling(image, size)
    size = (int(dst.shape[1] * 0.5), int(dst.shape[0] * 0.5))
    dst_4 = cv2.resize(image, size, 0, 0, cv2.INTER_LINEAR)

    dst[:size[1], :size[0]] = dst_4
    dst[size[1]:size[1] * 2, :size[0]] = dst_4

    dst_4 = cv2.flip(dst_4, 1)

    dst[:size[1], size[0]:size[0] * 2] = dst_4
    dst[size[1]:size[1] * 2, size[0]:size[0] * 2] = dst_4

    return dst


def division9(image):
    # size = (int(dst.shape[0] * 0.333), int(dst.shape[1] * 0.333), 3)
    # dst_9 = scaling(image, size)
    size = (int(image.shape[1] * 0.333), int(image.shape[0] * 0.333))
    dst_9 = cv2.resize(image, size, interpolation=cv2.INTER_LINEAR)

    dst = cv2.repeat(dst_9, 3, 3)

    return dst

import cv2 as cv
import numpy
from functools import reduce
import operator
import math


def crop(im):
    im = cv.resize(im, (600, 600))

    hsv_image = cv.cvtColor(im, cv.COLOR_BGR2HSV)
    lower_white = numpy.array([0, 0, 0], dtype=numpy.uint8)
    upper_white = numpy.array([150, 80, 255], dtype=numpy.uint8)
    mask = cv.inRange(hsv_image, lower_white, upper_white)
    contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

    approx = 0
    index1 = []

    for contour in contours:
        if 10000 < cv.contourArea(contour) < 250000:
            cnt_len = cv.arcLength(contour, True)
            approx = cv.approxPolyDP(contour, 0.02 * cnt_len, True)

    for i in range(4):
        index1.append(tuple(approx[i][0]))

    coordinates = index1
    center = tuple(map(operator.truediv, reduce(lambda x, y: map(operator.add, x, y), coordinates), [len(coordinates)] * 2))
    points = sorted(coordinates, key=lambda coord: (-135 - math.degrees(math.atan2(*tuple(map(operator.sub, coord, center))[::-1]))) % 360)

    pts1 = numpy.float32([points[0], points[1], points[2], points[3]])
    pts2 = numpy.float32([[0, 480], [480, 480], [480, 0], [0, 0]])

    matrix = cv.getPerspectiveTransform(pts1, pts2)
    result = cv.warpPerspective(im, matrix, (480, 480))

    return result

import cv2 as cv
import numpy


def drawredlines(result):
    hsv_result = cv.cvtColor(result, cv.COLOR_BGR2HSV)
    h, s, v = cv.split(hsv_result)
    chess_board = numpy.zeros((8, 8))
    squaresizex = result.shape[0] / 8
    squaresizex = int(round(squaresizex))
    squaresizey = result.shape[1] / 8
    squaresizey = int(round(squaresizey))

    for colomn in range(8):
        for row in range(8):

            i = int(row * squaresizex)
            pxl_list_r = []
            pxl_list_h = []
            while i < (row + 1) * squaresizex:
                j = int(colomn * squaresizey)
                while j < (colomn + 1) * squaresizey:
                    pxl_list_r.append(result[i, j][2])
                    pxl_list_h.append(h[i, j])

                    j += 1
                i += 1
            mean_r = numpy.mean(pxl_list_r)
            std_h = numpy.std(pxl_list_h)
            if std_h >= 3:
                chess_board[row][colomn] = 1

            txt2 = ''
            if chess_board[row][colomn] == 1 and 0 < mean_r < 80:   # Black squares
                if mean_r > 50:
                    txt2 = 'R'
                if mean_r <= 37:
                    txt2 = 'G'
            if chess_board[row][colomn] == 1 and 90 < mean_r < 160:  # White squares
                if mean_r > 130:
                    txt2 = 'R'
                if mean_r < 130:
                    txt2 = 'G'
            cv.putText(result, txt2, ((60 * colomn), (60 * row) + 25), 2, 1, (0, 255, 255))

    i = 0
    while i < result.shape[0]:
        j = 0
        while j < result.shape[1]:
            result[i, j] = (255, 0, 0)
            j += 1
        i += squaresizex
    j = 0
    while j < result.shape[1]:
        i = 0
        while i < result.shape[0]:
            result[i, j] = (255, 0, 0)
            i += 1
        j += squaresizey

    return chess_board

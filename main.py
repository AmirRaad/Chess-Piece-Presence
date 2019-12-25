import cv2 as cv
import croppingImage
import drawing

im1 = cv.imread("hkm.jpg")
im2 = cv.imread("hkm1.jpg")

result1 = croppingImage.crop(im1)
result2 = croppingImage.crop(im2)

horizontal = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
vertical = ['1', '2', '3', '4', '5', '6', '7', '8']

arr1 = drawing.drawredlines(result1)
arr2 = drawing.drawredlines(result2)
arr = arr2 - arr1
newR, newC = 0, 0
lastR, lastC = 0, 0
for row in range(8):
    for colomn in range(8):
        if arr[row][colomn] == 1:
            newR, newC = row, colomn
        if arr[row][colomn] == -1:
            lastR, lastC = row, colomn
pt1 = ((lastC+1)*60-30, (lastR+1)*60-30)
pt2 = ((newC+1)*60-30, (newR+1)*60-30)

if newR-lastR != 0 or newC-lastC != 0:
    print("Moved from", horizontal[lastC]+vertical[lastR], "to", horizontal[newC]+vertical[newR])
    cv.arrowedLine(result2, pt1, pt2, (0, 255, 255), 5)
else:
    print("There is no move yet!")

cv.imshow('hkm1', result1)
cv.imshow('hkm2', result2)

cv.waitKey(0)
cv.destroyAllWindows()

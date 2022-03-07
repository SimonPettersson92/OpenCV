import cv2 as cv
import numpy as np

img = cv.imread("Photos/cats 2.jpg")
cv.imshow("Cats", img)

blank = np.zeros(img.shape[:2], dtype="uint8")
cv.imshow("Blank image", blank)

mask_rectangle = cv.rectangle(
    blank.copy(),
    (img.shape[1] // 2, img.shape[0] // 2),
    (img.shape[1] // 2 - 200, img.shape[0] // 2 + 200),
    255,
    -1,
)
cv.imshow("Mask rectangle", mask_rectangle)

mask_circle = cv.circle(
    blank.copy(),
    (img.shape[1] // 2, img.shape[0] // 2),
    100,
    255,
    -1,
)
cv.imshow("Mask circle", mask_circle)

# First apply rectangular mask, then circular mask
masked_rectangle = cv.bitwise_and(img, img, mask=mask_rectangle)
cv.imshow("Masked rectangular image", masked_rectangle)

masked_circle = cv.bitwise_and(masked_rectangle, masked_rectangle, mask=mask_circle)
cv.imshow("Masked weird circular image", masked_circle)

# Generate intersection of a rectangle and circle and use as mask
rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(
    blank.copy(), (img.shape[1] // 2 + 45, img.shape[0] // 2 + 45), 100, 255, -1
)

weird_shape = cv.bitwise_and(rectangle, circle)
cv.imshow("Weird shape", weird_shape)

masked = cv.bitwise_and(img, img, mask=weird_shape)
cv.imshow("Masked", masked)

cv.waitKey(0)

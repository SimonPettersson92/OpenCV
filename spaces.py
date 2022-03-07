import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("Photos/park.jpg")
cv.imshow("Park", img)

# Display with matplotlib gives inverse because OpenCV uses BGR colour format
plt.imshow(img)
plt.show()

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("LAB", lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)

# LAB to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow("LAB to BGR", lab_bgr)

# LAB to BGR to HSV
lab_bgr_hsv = cv.cvtColor(lab_bgr, cv.COLOR_BGR2HSV)
cv.imshow("LAB to BGR to HSV", lab_bgr_hsv)

# After converting to RGB, matplotlib displays the correct image
plt.imshow(rgb)
plt.show()

cv.waitKey(0)

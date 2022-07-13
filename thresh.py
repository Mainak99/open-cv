import cv2 as cv

img = cv.imread('photos/cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray )

# # Simple Thresholding
# threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
# # this sets all the pixel which have pixel intensity above 150 to pixel intensity of 255 in the thresh image and the rest as 0 pixel intensity
# cv.imshow('Simple Thresholded', thresh)

# threshold, thresh_inv= cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
# # this sets all the pixel which have pixel intensity below 150 to pixel intensity of 255 in the thresh image and the rest as 0 pixel intensity
# # i.e the inverse of the previous one
# cv.imshow('Simple Thresholded Inverse', thresh_inv)

# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive Thresholding', adaptive_thresh)

adaptive_thresh_inv = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 3)
cv.imshow('Adaptive Thresholding Inverse', adaptive_thresh_inv)


cv.waitKey(0)

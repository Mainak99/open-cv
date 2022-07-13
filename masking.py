import cv2 as cv
import numpy as np
# 1st comment --> the dimensions of the mask has to be the same size as that of the image for masking to work

img = cv.imread('photos/cats2.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
# blank = np.zeros((300,300), dtype='uint8') 
# ^--> this line won't work instead of the first line because of the 1st comment
cv.imshow('Blank Image', blank)

# Circlular mask
# mask = cv.circle(blank, (img.shape[1]//2+30, img.shape[0]//2), 100, 255, -1)
# cv.imshow('Mask', mask)

circle=cv.circle(blank.copy(), (img.shape[1]//2+45, img.shape[0]//2), 100, 255, -1)
rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1) 

wierd_shape = cv.bitwise_and(circle,rectangle)
cv.imshow('Wierd Shape', wierd_shape)

# # Rectangular mask
# mask = cv.rectangle(blank, (img.shape[1]//2,img.shape[0]//2), (img.shape[1]//2 + 100, img.shape[0]//2 + 100), 255, -1)
# cv.imshow('Mask', mask)

masked = cv.bitwise_and(img, img, mask=wierd_shape)
cv.imshow('Masked Image', masked)

cv.waitKey(0)
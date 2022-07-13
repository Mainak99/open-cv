import cv2 as cv
import numpy as np

img = cv.imread('photos/park.jpg')
cv.imshow('Park',img)

blank = np.zeros(img.shape[:2],dtype='uint8')


b,g,r = cv.split(img) # The normal image has color channel of 3 :- red, green and blue

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Red',red) # the red one has color channel 1, it shows a grayscale image :- same for green and blue
cv.imshow('Green',green) 
cv.imshow('Blue',blue)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)  

 
merged = cv.merge([b,g,r]) 
cv.imshow('Merged',merged)

cv.waitKey(0)
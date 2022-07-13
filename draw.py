import cv2 as cv
import numpy as np

# img = cv.imread('photos/naruto.jpg')
# cv.imshow('Cat',img)

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank',blank)

# 1. Paint the whole image a certian colour
# blank[200:300, 300:400] = 0,0,255
# cv.imshow('Green',blank)

# 2. Draw a rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,250,0), thickness=cv.FILLED) # thickness = cv.FILLED fills the inside of the triangle with the same colour, 
# thickness = -1 also fills the inside of the triangle)
cv.imshow('Rectangle',blank)

# 3. Draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 80, (0,0,255), thickness=-1)
cv.imshow('Circle', blank) 

# 4. Draw a line
cv.line(blank, (100,250), (300,400), (255,255,255), thickness=3)
cv.imshow('Line', blank)

# 5. Write text
cv.putText(blank, 'Hello, my name is Mainak!!!', (0,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)
 
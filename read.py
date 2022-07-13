import cv2 as cv

img = cv.imread('photos/naruto2.jpg')

cv.imshow('Cat', img)

# Reading videos
# when video is captured from the camera, instead of location we provide integer digits inside bracket, (ex. 0 if your recording from the computer webcam)

capture = cv.VideoCapture('videos/drone.mp4') 

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    
    if cv.waitKey(20) & 0xFF==('d'):
        break

capture.release()
cv.destroyAllWindows()

# error: (-215:Assertion failed) is shown when openCV cannot find any media file in the specified location. 
# After video file is completed playing it shows that error which means it has run out of frames to read.
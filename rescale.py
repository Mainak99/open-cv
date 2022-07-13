import cv2 as cv

img = cv.imread('photos/naruto.jpg')
cv.imshow('Naruto', img)

def rescaleFrame(frame, scale=0.75):
    # this will work for Images, Video and Live Video
    width = int(frame.shape[1] * scale) # frame.shape[1] is the width of the image (data type is int)
    height = int(frame.shape[0] * scale) # frame.shape[0] is the height of the image 
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)

def changeRes(width,height):
    # This will only work for live video
    capture.set(3,width)
    capture.set(4,height) # 3,4 and refer to the properties of the capture class i.e width and height respectively

# Reading videos
capture = cv.VideoCapture('videos/drone.mp4') 

while True:
    isTrue, frame = capture.read()
    
    frame_resized = rescaleFrame(frame, scale=.2)

    # cv.imshow('Video', frame)

    # cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==('d'):
        break

capture.release()
cv.destroyAllWindows()
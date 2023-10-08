import cv2 as cv
cam=cv.VideoCapture(0) #to capture video, 0 for default camera
while True:
    __,frame=cam.read()   #to read frame
    print(frame.shape)    #to print frame
    hei,weg,__=frame.shape
    cv.rectangle(frame,(140,220),(340,420),(255,255,0),1)   #to take shape in image
    cv.imshow("Result",frame)         #to show result as name of frame
    cv.imwrite("image.png",frame)     #to save frame 
    if (cv.waitKey(1) == ord('q')):   #to return from image
        break

cam.release()
cv.destroyAllWindows()




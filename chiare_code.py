# __author__ = 'chiarehwang'

import cv2
import numpy as np
import cv2.cv as cv


cam = cv2.VideoCapture(0)
print(cam.get(3))
print(cam.get(4))
#print(cam.read())

x = 635
c = x  #column
w = 10
y = 355
r = y  #row
h = 10

ret, frame = cam.read()
calibratedRoi = frame[r:r + h, c:c + w]  #region of interest
#print(calibratedRoi)

calibratedMean = np.mean(calibratedRoi)
print(calibratedMean)

while (True):
    # Capture frame-by-frame
    ret, frame = cam.read()
    roi = frame[r:r + h, c:c + w]  #region of interest
    mean = np.mean(roi)
    diff = mean - calibratedMean

    #Draw rectangle around light detecting pixels
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('blobber', frame)

    if abs(diff) > 20: #FYI If lighting conditions change this breaks
        ##TAKE A PICTURE
        cv.NamedWindow("camera", 1)
        capture = cv.CaptureFromCAM(0)
        img = cv.QueryFrame(capture)
        cv.ShowImage("camera", img)
        #break


    if cv2.waitKey(1) & 0xFF == ord('q'): #Hit Q to end
        break

cam.release()
cv2.destroyAllWindows()

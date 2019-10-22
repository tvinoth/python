import numpy as np
import cv2

cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()
fourcc = cv2.VideoWriter_fourcc(*'XVID')
secd = cv2.VideoWriter('video.avi',fourcc, 20.0, (640,480))
out = cv2.VideoWriter('video1.avi',fourcc, 20.0, (640,480))

while(1):
    ret, frame = cap.read()
    out.write(frame)

    fgmask = fgbg.apply(frame)
    secd.write(fgmask)
    cv2.imshow('fgmask',frame)
    cv2.imshow('frame',fgmask)

    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    
secd.release()
cap.release()
cap.release()
cv2.destroyAllWindows()
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    #frame = cv2.resize(frame,(640,480))

    #operations on the frame come here
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower = np.array([0,120,70])
    upper = np.array([180,255,255])
    mask0 = cv2.inRange(hsv, lower, upper)


    #join masks
    lower = np.array([170,120,70])
    upper = np.array([180,255,255])
    mask1 = cv2.inRange(hsv, lower, upper)


    #join
    mask = mask0 + mask1
    cv2.bitwise_and(frame, frame, mask=mask)
    
    #erosion, dilation, and blur
    frame = cv2.erode(frame, None, iterations=2)
    frame = cv2.dilate(frame, None, iterations=2)
    frame = cv2.GaussianBlur(frame, (13,13), 0)
    
    #find contours
    cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    #Bounding rectangle
    for c in cnts:
          x,y,w,h = cv2.boundingRect(c)
          aspect_ratio = float(w)/h
          area = float(w*h)
          if .8 <= aspect_ratio <= 1.3 and area>1000:
              cv2.rectangle(frame, (x, y), (x + w, y + h), (36,255,12), 2)



    # Display the resulting frame
    cv2.imshow('frame',frame)
    cv2.imshow('mask', mask)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
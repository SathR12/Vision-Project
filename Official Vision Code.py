#import modules
import numpy as np
import cv2

#image resizing and blurring
img = cv2.imread(input("Image"))
original_resize = cv2.resize(img, (640,480))
resize = cv2.resize(img, (640,480))

#HSV conversion and mask
hsv = cv2.cvtColor(resize, cv2.COLOR_BGR2HSV)
lower = np.array([0,70,0])
upper = np.array([255, 255, 255])


#create mask and dilate
mask = cv2.inRange(hsv, lower, upper)
cv2.bitwise_and(resize, resize, mask=mask)

#erosion, dilation, and blur
resize = cv2.erode(resize, None, iterations=2)
resize = cv2.dilate(resize, None, iterations=2)
resize = cv2.GaussianBlur(resize, (13,13), 0)


#find contours
cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

#Bounding rectangle
for c in cnts:
    x,y,w,h = cv2.boundingRect(c)
    aspect_ratio = float(w)/h
    if .9 <= aspect_ratio <= 1.10:
        cv2.rectangle(original_resize, (x, y), (x + w, y + h), (36,255,12), 2)
    print(aspect_ratio)



    
#show images
cv2.imshow('b,d,e', resize)
cv2.imshow('mask', mask)
cv2.imshow('HSV', hsv)
cv2.imshow('apple', original_resize)




cv2.waitKey()

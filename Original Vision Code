#import modules
import numpy as np
import cv2

#image resizing and blurring
img = cv2.imread(input("image"))
resize_img = cv2.resize(img, (640,480))
blur_image = cv2.fastNlMeansDenoisingColored(resize_img,None,20,10,7,21)

#conversion to HSV
rgb_img = cv2.cvtColor(resize_img, cv2.COLOR_BGR2HSV)

#color range and kernel
kernel = np.ones((5,5))
lower = np.array([0,70,0])
upper = np.array([255,255,255])

#create mask and dilate
mask = cv2.inRange(rgb_img, lower, upper)
img_dilation = cv2.dilate(mask, kernel, iterations=1)


#find contours
cnts = cv2.findContours(img_dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

#Bounding rectangle
for c in cnts:
    x,y,w,h = cv2.boundingRect(c)
    aspect_ratio = float(w/h)
    if .9< aspect_ratio < 1.8:
        cv2.rectangle(resize_img, (x, y), (x + w, y + h), (36,255,12), 2)
    print(aspect_ratio)
    
#show images
cv2.imshow('apples', resize_img)
cv2.imshow('mask', img_dilation)
cv2.imshow('HSV', rgb_img)
cv2.waitKey()

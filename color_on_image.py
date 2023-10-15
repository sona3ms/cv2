import cv2
import numpy as np
def click_event(event, x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        blue = img[x,y,0]
        green = img[x,y,1]
        red = img[x,y,2]
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        mycolor = np.zeros((512,512,3),np.uint8)
        mycolor[:]=[blue,green,red]
        cv2.imshow('color',mycolor)

img = cv2.imread(r'C:\Users\HP\Downloads\Week-17-vs\lena.jpg')
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
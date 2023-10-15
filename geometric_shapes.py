import cv2
import numpy as np
#img = cv2.imread(r'C:\Users\HP\Downloads\Week-17-vs\lena.jpg')
#numpy
img = np.zeros([512,512,3],np.uint8)



#line
#img = cv2.line(img,(0,0),(255,255),(255,0,0),2)
#img = cv2.arrowedLine(img,(0,255),(255,255),(20,56,100),2)

#rectangle
#img = cv2.rectangle(img,(384,0),(510,128),(0,0,255),2)

#circle
#img = cv2.circle(img,(477,63),63,(0,255,0),-1)

#ellipse
#center,axes,angle,start_angle,end_angle,color,thickness
#img = cv2.ellipse(img,(200,200),(100,100),0,0,180,(0,255,0),-1)

#add text
font =cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img,'opencv',(10,500),font,4,(255,255,255),10,cv2.LINE_AA)


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
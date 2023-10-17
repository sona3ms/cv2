# #read
import cv2
import numpy as np
# import datetime
import matplotlib.pyplot as plt

# # cap = cv2.VideoCapture(0)
# # while True:
# #     ret, frame=cap.read()
# #     font = cv2.FONT_HERSHEY_SIMPLEX
# #     d = str(datetime.datetime.now())
# #     frame = cv2.putText(frame,d,(10,100),font,3,(0,0,0))
# #     if not ret:
# #         print("Error:could not read a frame")
# #         break
# #     cv2.imshow('Live stream',frame)
# img = cv2.imread(r'C:\Users\HP\Downloads\Week-17-vs\lena.jpg',cv2.IMREAD_GRAYSCALE)
# #img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# #img = cv2.rectangle(img,(10,10),(100,500),(255,255,255),3)
# #img = cv2.circle(img,(200,300),30,(255,255,255),1)
    
# # img = cv2.putText(img,'hello cv',(10,500),font,5,(0,0,0),cv2.LINE_AA)
   

# cv2.imshow('image',img)
# # # cv2.imwrite('new_img.png',img)
#     # if cv2.waitKey(1) & 0xFF == ord('q'):
#     #     break

# img = np.zeros((512,512),dtype=np.uint8)
# plt.imshow(img,cmap='gray')
# plt.show()
img = cv2.imread(r'C:\Users\HP\Downloads\Week-17-vs\lena.jpg')
# def click_event(event,x,y,flags,param):
#     if event == cv2.EVENT_LBUTTONDOWN :
#         print(x,',',y)
#         strxy = str(x) +''+str(y)
#         font = cv2.FONT_HERSHEY_SIMPLEX
#         cv2.putText(img,strxy,(x,y),font,1,(0,0,0),cv2.LINE_AA)
#         cv2.imshow('image',img)
#     if event == cv2.EVENT_RBUTTONDBLCLK:
#         b = img[y,x,0]
#         g= img[y,x,1]
#         r= img[y,x,2]
#         font = cv2.FONT_HERSHEY_SIMPLEX
#         strbgr = str(b)+' '+str(g)+' '+str(r)
#         cv2.putText(img,strbgr,(x,y),font,2,(0,0,0),2,cv2.LINE_AA)
#         cv2.imshow('image',img)
# cv2.setMouseCallback('image',click_event)
# img = cv2.resize(img,(200,200))

# [b,g,r]=cv2.split(img)
# cv2.imshow('blue_image',b)
# cv2.imshow('green channel',g)
# cv2.imshow('red channel',r)
# m=cv2.merge([b,g,r])
# cv2.imshow('merged',m)

def empty_fn(x):
    pass
image = np.zeros((300,500,3),dtype=np.uint8)
cv2.namedWindow('image')
cv2.createTrackbar('b','image',0,100,empty_fn)
cv2.createTrackbar('c','image',1,100,empty_fn)
cv2.createTrackbar('blue','image',0,255,empty_fn)
cv2.createTrackbar('green','image',0,255,empty_fn)
cv2.createTrackbar('red','image',0,255,empty_fn)

while True:
    b = cv2.getTrackbarPos('b','image')
    c = cv2.getTrackbarPos('c','image')
    blue = cv2.getTrackbarPos('blue','image')
    green = cv2.getTrackbarPos('green','image')
    red = cv2.getTrackbarPos('red','image')
    ad=cv2.convertScaleAbs(image,alpha =c/50.0,beta=b)
    # ad[:,:,0]=blue
    # ad[:,:,1]=green
    # ad[:,:,2]=red
    cv2.imshow('image',ad)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# cv2.waitKey(0)
cv2.destroyAllWindows()
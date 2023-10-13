import cv2 as cv
import numpy as np

def nothing(x):
   pass

#In the following section i'm creating a tracking
#window where all my trackbars are going to be present
#in
cv.namedWindow('tracking')
cv.createTrackbar('LH','tracking',0,255,nothing)
cv.createTrackbar('LS','tracking',0,255,nothing)
cv.createTrackbar('LV','tracking',0,255,nothing)
cv.createTrackbar('UH','tracking',255,255,nothing)
cv.createTrackbar('US','tracking',255,255,nothing)
cv.createTrackbar('UV','tracking',255,255,nothing)


#The loop is set to run infinitely so that the image 
#in the window will be refreshed every microsecond
while True:
    image=cv.imread(r'C:\Users\HP\Downloads\Week-17-vs\lena.jpg')
    hsv=cv.cvtColor(image,cv.COLOR_BGR2HSV)
    
    #In the following lines the value from the track
    #bars are set to the variables of upper and lower 
    #limits of the various features
    l_h=cv.getTrackbarPos('LH','tracking')
    l_s=cv.getTrackbarPos('LS','tracking')
    l_v=cv.getTrackbarPos('LV','tracking')
    u_h=cv.getTrackbarPos('UH','tracking')
    u_s=cv.getTrackbarPos('US','tracking')
    u_v=cv.getTrackbarPos('UV','tracking')
    
    #The values are then made into 2 arrays 
    #as upper and lower bounds respectively
    l_b=np.array([l_h,l_s,l_v])
    u_b=np.array([u_h,u_s,u_v])
    
    #The upper and lower bounds are then made into
    #a mask such that only the parts satisfying the 
    #specific parameters will be displayed rest will 
    #given the value of 0
    mask=cv.inRange(hsv,l_b,u_b)
    #mask gives out the x and y coordinates of the 
    #pixels to be shown
    res=cv.bitwise_and(image,image,mask=mask)
    
    cv.imshow('Image',image)
    cv.imshow('Mask',mask)
    cv.imshow('Result',res)
    # cv.imshow('tracking',image)
    if cv.waitKey(1)==ord('q'):
        break
cv.destroyAllWindows()

#blue->lb->[94,112,83]
#blue->ub->[156,255,255]
#red->lb->[0,230,150]
#red->ub->[10,255,242]
#green->lb->[64,47,176]
#green->ub->[84,255,255]
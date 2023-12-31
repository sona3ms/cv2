import cv2
import  numpy as np
# Create an empty function for the trackbar
def nothing(x):
    print(x)


#img = np.zeros((300,512,3),np.uint8)

cv2.namedWindow('image')

cv2.createTrackbar('B','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('R','image',0,255,nothing)

while True:
    img = cv2.imread(r'C:\Users\HP\Downloads\Week-17-vs\lena.jpg')
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    cv2.imshow('image',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    b = cv2.getTrackbarPos('B','image')  
    g = cv2.getTrackbarPos('G','image')
    r = cv2.getTrackbarPos('R','image') 

    img[:] = [b,g,r]
cv2.destroyAllWindows()

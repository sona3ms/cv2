import cv2
img = cv2.imread('lena.jpg')
blue =img[:,:,0]
green =img[:,:,1]
red = img[:,:,2]
color_image = cv2.merge([blue, green, red])
cv2.imshow('image',color_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
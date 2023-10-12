import cv2
img = cv2.imread('lena.jpg')
b = img[:,:,0]
zeros = 0 * b
blue =cv2.merge((b,zeros,zeros))
green =cv2.merge((zeros,b,zeros))
red = cv2.merge((zeros,zeros,b))
cv2.imshow('green',green)
cv2.imshow('blue',blue)
cv2.imshow('red',red)
cv2.waitKey(0)
cv2.destroyAllWindows()
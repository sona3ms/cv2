import cv2

img = cv2.imread(r'C:\Users\HP\Downloads\Week-17-vs\messi.jpg')
img = cv2.resize(img,(640,480))
img2 = cv2.imread(r'C:\Users\HP\Downloads\Week-17-vs\lena.jpg')
img2 = cv2.resize(img2,(640,480))
# b,g,r = cv2.split(img)
# img = cv2.merge((b,g,r))

new_img= cv2.add(img,img2)
#weight
new_img = cv2.addWeighted(img,0.8,img2,.2,0)
cv2.imshow('image',new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()






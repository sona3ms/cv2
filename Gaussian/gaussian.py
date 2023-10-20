import cv2

image = cv2.imread('lena.jpg')
pyramid = [image]

for i in range(6):
    image = cv2.pyrDown(image)
    pyramid.append(image)

# # Display each level of the pyramid one by one
for i, level in enumerate(pyramid):
    cv2.imshow(f'Level {i}', level)
# lr = cv2.pyrDown(image)
# lr1 = cv2.pyrUp(lr)
# cv2.imshow('original',image)
# cv2.imshow('1',lr)
# cv2.imshow('2',lr1)
# Wait for a key press and close OpenCV windows
cv2.waitKey(0)
cv2.destroyAllWindows()

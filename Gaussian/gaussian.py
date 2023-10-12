import cv2

image = cv2.imread('lena.jpg')
pyramid = [image]

for i in range(6):
    image = cv2.pyrDown(image)
    pyramid.append(image)

# Display each level of the pyramid one by one
for i, level in enumerate(pyramid):
    cv2.imshow(f'Level {i}', level)

# Wait for a key press and close OpenCV windows
cv2.waitKey(0)
cv2.destroyAllWindows()

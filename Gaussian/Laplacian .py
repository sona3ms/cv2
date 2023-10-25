import cv2
import numpy as np

image = cv2.imread(r'C:\Users\HP\Downloads\Week-17-vs\Merge,split,resize\lena.jpg',0)

# Created an empty list to store pyramid levels
pyramid = [image]

for i in range(3):
    image = cv2.pyrDown(image)
    pyramid.append(image)

laplacian_pyramid = [pyramid[3]]  

for i in range(3, 0, -1):
    expanded = cv2.pyrUp(pyramid[i])
    laplacian = cv2.subtract(pyramid[i - 1], expanded)
    laplacian_pyramid.append(laplacian)

for i, level in enumerate(laplacian_pyramid):
    cv2.imshow(f'level{i}',level)

cv2.waitKey(0)
cv2.destroyAllWindows()

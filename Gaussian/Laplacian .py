import cv2
import numpy as np

# Load the original image
image = cv2.imread(r'C:\Users\HP\Downloads\Week-17-vs\Merge,split,resize\lena.jpg')

# Create an empty list to store pyramid levels
pyramid = [image]

# Generate a 4-level Gaussian pyramid
for i in range(3):
    image = cv2.pyrDown(image)
    pyramid.append(image)

# Create an empty list to store the Laplacian pyramid
laplacian_pyramid = [pyramid[3]]  # The highest resolution image in the Gaussian pyramid

# Generate the Laplacian pyramid
for i in range(3, 0, -1):
    expanded = cv2.pyrUp(pyramid[i])
    laplacian = cv2.subtract(pyramid[i - 1], expanded)
    laplacian_pyramid.append(laplacian)

# Display the Laplacian pyramid levels
for i, level in enumerate(laplacian_pyramid):
    cv2.imshow(f'Laplacian Level {i}', level)

# Wait for a key press and close OpenCV windows
cv2.waitKey(0)
cv2.destroyAllWindows()

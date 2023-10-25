# import cv2
# import matplotlib.pyplot as plt
# import datetime
import cv2
import numpy as np

# Read an image
image = cv2.imread(r"C:\Users\HP\Downloads\Week-17-vs\lena.jpg")

# Define the shearing parameters (shearing in the x-axis)
shear_factor = 0.5  # Adjust the value as needed
rows, cols, _ = image.shape

# Define the shear matrix
shear_matrix = np.array([[1, shear_factor, 0],[0, 1, 0]], dtype=np.float32)

# Apply the shear transformation
sheared_image = cv2.warpAffine(image, shear_matrix, (cols, rows))

# Display the original and sheared images
cv2.imshow('Original Image', image)
cv2.imshow('Sheared Image', sheared_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# font = cv2.FONT_HERSHEY_SIMPLEX
# date_ = str(datetime.datetime.now())
# img = cv2.putText(img,date_,(10,500),font,1,(0,0,0),1)
# cv2.imshow('img',img)


# cv2.waitKey(0)
# cv2.destroyAllWindows()

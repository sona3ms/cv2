import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread(r'C:\Users\HP\Downloads\Week-17-vs\lena.jpg')

height, width = img.shape[:2]
# dx,dy= 100,100
# mat_img = np.float32([[1,0,dx],[0,1,dy]])
# new_img = cv2.warpAffine(img,mat_img,(width,height))
# cv2.imshow('orginal',img)
# cv2.imshow('new_img',new_img)
#rotation
# angle = 45  # Degrees
# center = (width // 2, height // 2)
# rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1)
# rotated_image = cv2.warpAffine(img, rotation_matrix, (width, height))
# cv2.imshow('rotated_image',rotated_image)
#scaling
scale_x, scale_y = 1, 0.5  #(.5,.5)->50% scaling

# Apply the scaling
scaled_image = cv2.resize(img, None, fx=scale_x, fy=scale_y, interpolation=cv2.INTER_LINEAR)
cv2.imshow('scaled_image',scaled_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
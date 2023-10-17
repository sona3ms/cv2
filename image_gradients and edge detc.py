import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r'C:\Users\HP\Downloads\Week-17-vs\Blender_Suzanne1.jpg')
lap = cv2.Laplacian(img,cv2.CV_64F,ksize=3)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
combined = cv2.bitwise_or(sobelx,sobely)
canny = cv2.Canny(img,100,200)
titles=['image','Laplacian','sobelx','sobely','combined','canny']
images = [img,lap,sobelx,sobely,combined,canny]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis('off')

plt.show()
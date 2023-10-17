import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread(r'C:\Users\HP\Downloads\Week-17-vs\lena.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5,5),np.float32)/25
#homogenious
dst = cv2.filter2D(img,-1,kernel)
blur_ = cv2.blur(img,(15,15))
Gaussian_ = cv2.GaussianBlur(img,(15,15),0)
median_ = cv2.medianBlur(img,15)
bilateral=cv2.bilateralFilter(img,9,75,75)
titles = ['image','2D Convolution','Averaging_blur','Gaussian_Blurring','Median_Blurring','Bilateral Filtering']
images = [img,dst,blur_,Gaussian_,median_,bilateral]



for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.axis('off')
plt.show()
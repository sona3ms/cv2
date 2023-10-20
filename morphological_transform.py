import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('j_morph.png')#already B&W image

kernal = np.ones((5,5),np.uint8)

dilation = cv2.dilate(img,kernal,iterations=2)
erosion = cv2.erode(img,kernal,iterations=2)
opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernal)
closing = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernal)
gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernal)
tophat = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernal)
blackhat = cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernal)



titles = ['image','dilation','erosion','opening','closing','gradient','tophat','blackhat']
images = [img,dilation,erosion,opening,closing,gradient,tophat,blackhat]

for i in range(8):
    plt.subplot(3,3,i+1), plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis('off')
plt.show()
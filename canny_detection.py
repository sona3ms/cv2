import cv2
from matplotlib import pyplot as plt

img = cv2.imread(r'C:\Users\HP\Downloads\Week-17-vs\lena.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
canny = cv2.Canny(img,100,200)
titles =['image','canny']
images = [img,canny]
for i in range(2):
    plt.subplot(1,2,1+i),plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis('off')
plt.show()
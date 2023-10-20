# import matplotlib.pyplot as plt
# import cv2
# img = cv2.imread('lena.jpg')
# img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# plt.imshow(img)
# plt.axis('off')
# plt.show()
import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r'lena.jpg', 0)
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist)
plt.title('Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.savefig('save.png')
plt.show()

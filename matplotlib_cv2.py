from matplotlib import pyplot as plt
import cv2

img = cv2.imread(r'C:\Users\HP\Downloads\Week-17-vs\lena.jpg')
cv2.imshow('image',img)

#converting to RGB format
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.axis('off')
plt.imshow(img)
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()
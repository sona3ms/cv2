import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r'C:\Users\HP\Downloads\Week-17-vs\lena.jpg')
#Gaussian Noise
noise = np.random.normal(0,25,img.shape).astype(np.uint8)
noisy_img = cv2.add(img, noise)
gas = cv2.GaussianBlur(noisy_img,(15,15),0)
#salt and paper
salt = np.zeros(img.shape,np.uint8)
cv2.randn(salt,128,30)
salt_img = cv2.add(img,salt)
denoised_image = cv2.medianBlur(salt_img, 5)
#speckle noise
speckle = np.random.normal(0,25,img.shape).astype(np.uint8)
spe = img + img * speckle / 255.0
spe = spe.astype(np.uint8)
spe_denoised_image = cv2.bilateralFilter(spe, 9, 75, 75)

titles=['original','gaussian Noise','salt and pepper','speckle Noise','gaus-clean','salt-clean','speckle-clean']
images=[img,noisy_img,salt_img,spe,gas,denoised_image,spe_denoised_image]

for i in range(7):
    plt.subplot(3,3,i+1)
    plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
    plt.title(titles[i])
    plt.axis('off')
plt.show()

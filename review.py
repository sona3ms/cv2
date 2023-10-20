import cv2
import matplotlib.pyplot as plt
img=cv2.imread(r'C:\Users\HP\Downloads\Week-17-vs\lena.jpg',0)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
line_ = cv2.line(img,(50,50),(400,100),(255,255,255),2)
cv2.imshow('image',line_)
# plt.imshow(img)
# plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
# import cv2

# # Read the image in grayscale
# img = cv2.imread(r'C:\Users\HP\Downloads\Week-17-vs\lena.jpg', 0)

# # Draw a white line on the image
# line_img = cv2.line(img, (50, 50), (400, 100), (255, 255, 255), 2)

# # Display the image
# cv2.imshow('image', line_img)

# # Wait for a key event and then close the window
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2

# Load the original image
image = cv2.imread(r'C:\Users\HP\Downloads\Week-17-vs\Merge,split,resize\lena.jpg')

# Create an empty list to store pyramid levels
pyramid = [image]

# Generate a 4-level Gaussian pyramid
for i in range(3):
    image = cv2.pyrDown(image)
    pyramid.append(image)

# Display the pyramid levels
for i, level in enumerate(pyramid):
    cv2.imshow(f'Level {i}', level)

# Wait for a key press and close OpenCV windows
cv2.waitKey(0)
cv2.destroyAllWindows()

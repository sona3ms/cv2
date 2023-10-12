import cv2
img = cv2.imread('lena.jpg')
blue, green, red = cv2.split(img)
cv2.imshow('Blue Channel', blue)
cv2.imshow('Green Channel', green)
cv2.imshow('Red Channel', red)
cv2.waitKey(0)
cv2.destroyAllWindows()



# import cv2
# # Load two images
# image1 = cv2.imread('lena.jpg')
# image2 = cv2.imread('lena.jpg')

# # Check if the images have the same dimensions
# if image1.shape == image2.shape:
#     # Combine the images side by side
#     combined_image = cv2.hconcat([image1, image2])

#     # Display the combined image
#     cv2.imshow('Combined Image', combined_image)

#     # Wait for a key press and close the window when any key is pressed
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
# else:
#     print("The images have different dimensions and cannot be combined.")

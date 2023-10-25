# YOLO object detection
import cv2 as cv
import numpy as np
import time

img = cv.imread(r'C:\Users\HP\Downloads\Week-17-vs\horse.jpg')
cv.imshow('window',  img)
cv.waitKey(1)

# Give the configuration and weight files for the model and load the network.
net = cv.dnn.readNetFromDarknet(r'C:\Users\HP\Downloads\Week-17-vs\yolov3.cfg', 'yolov3.weights')
net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
# net.setPreferableTarget(cv.dnn.DNN_TARGET_CPU)

ln = net.getLayerNames()
print(len(ln), ln)

# construct a blob from the image
blob = cv.dnn.blobFromImage(img, 1/255.0, (416, 416), swapRB=True, crop=False)
r = blob[0, 0, :, :]

cv.imshow('blob', r)
text = f'Blob shape={blob.shape}'
cv.displayOverlay('blob', text)
cv.waitKey(1)

net.setInput(blob)
t0 = time.time()
outputs = net.forward(ln)
t = time.time()
# Loop through the outputs and draw bounding boxes and labels
for output in outputs:
    for detection in output:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5:  # Adjust the confidence threshold as needed
            center_x = int(detection[0] * img.shape[1])
            center_y = int(detection[1] * img.shape[0])
            width = int(detection[2] * img.shape[1])
            height = int(detection[3] * img.shape[0])

            # Calculate the coordinates for the top-left corner of the bounding box
            x = int(center_x - width / 2)
            y = int(center_y - height / 2)

            # Draw a bounding box and label
            color = (0, 255, 0)  # BGR color for the box (green in this case)
            cv.rectangle(img, (x, y), (x + width, y + height), color, thickness=2)
            label = f'Class: {class_id}, Confidence: {confidence:.2f}'
            cv.putText(img, label, (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, color, thickness=2)

# Display the image with bounding boxes and labels
cv.displayOverlay('window', f'forward propagation time={t-t0}')
cv.imshow('window', img)
cv.waitKey(0)
cv.destroyAllWindows()

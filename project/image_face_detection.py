import cv2

# Load the pre-trained Haar Cascade XML file for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_objects(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect objects (faces) in the image
    objects = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
    
    return objects

# Function to draw rectangles around detected objects
def draw_objects(image, objects):
    for (x, y, w, h) in objects:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)

# Image detection
#image_path = r'C:\Users\HP\Downloads\Week-17-vs\project\img1.jpg' 
image_path = r'C:\Users\HP\Downloads\Week-17-vs\project\test4.jpg'
image = cv2.imread(image_path)
if image is not None:
    detected_objects = detect_objects(image)
    draw_objects(image, detected_objects)
    cv2.imshow('Object Detection in Image', image)
    cv2.waitKey(0)
else:
    print("Failed to load the image.")


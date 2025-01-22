# import cv2

# face_cap=cv2.CascadeClassifier('C:/Users/MD SHAFIUL ISLAM/AppData/Roaming/Python/Python312/site-packages/cv2/haarcascade_frontalface_default.xml')
# vedio=cv2.VideoCapture(0)
# while True:
#     ret,vedio1=vedio.read()
#     col=cv2.cvtColor(vedio1,cv2.COLOR_BGR2GRAY)
#     faces=face_cap.detectMultiScale(
#         col,
#         scaleFactor=1.1,
#         minNeighbors=5,
#         minSize=(30,30),
#         flags=cv2.CASCADE_SCALE_IMAGE
#     )
#     for (x,y,w,h) in faces:
#         cv2.rectangle(vedio1,(x,y),(x+w,y+h),(0,255,0),2)
#     cv2.imshow('vedio live',vedio1)
#     if cv2.waitKey(10) == ord('a'):
#         break
# vedio.release()

import cv2

# Load the pre-trained Haar Cascade classifier
face_cap = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start video capture from the webcam
video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    
    if not ret:
        print("Failed to capture video")
        break
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cap.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    
    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Display the video with detected faces
    cv2.imshow('Video Live', frame)
    
    # Break the loop if 'a' is pressed
    if cv2.waitKey(10) == ord('a'):
        break

# Release the video capture object and close all windows
video.release()
cv2.destroyAllWindows()

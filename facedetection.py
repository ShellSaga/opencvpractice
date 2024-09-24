# using Haar Cascades pre-trained model for detecting objects

import cv2

# initalize and load Haar Cascades
# error with opencv on system - manually added file to directory and called again# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
    #c apture frame by frame
    ret, frame = cap.read()

    if not ret: 
        break
    # will break progrmam if video capture fails for some reason

    # Haar Cascades is usually done on grayscale images/videos - convert video to grayscale
    grayscaled = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect faces in frame
    face_detect = face_cascade.detectMultiScale( grayscaled, 1.3, 5)

    #draw rectangle around detected faces
    for (x, y, w, h) in face_detect:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # display frame with detected faces
    cv2.imshow('Face Detection', frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
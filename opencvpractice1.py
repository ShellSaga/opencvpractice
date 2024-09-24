import cv2

# Open the default camera (usually the built-in webcam)
cap = cv2.VideoCapture(0)
# if using a external camera replace the (0) with (1)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Capture and display video
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If frame is read correctly ret is True
    if not ret:
        print("Error: Can't receive frame (stream end?). Exiting ...")
        break

    # Display the resulting frame
    cv2.imshow('Camera Feed', frame)
    
    # takes photo of camera frame
    while cv2.waitKey(0) == ord('c'):
        cv2.imwrite('new_img.jpg',frame)
    # Press 'q' to quit
    if cv2.waitKey(0) == ord('q'):
        break

# Release the capture and destroy windows
cap.release()
cv2.destroyAllWindows()
# import cv2

# # Define the codec and create a VideoWriter object
# cap = cv2.VideoCapture(0)
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')

# # 30.0 is the frames per second(fps) and (640,480) is the frame size.
# out = cv2.VideoWriter('output.mp4', fourcc, 30.0, (640,480))

# while True:
#     ret, frame = cap.read()
#     if ret:
#         # Write the frame to the video file
#         out.write(frame)
#         # Display the frame
#         cv2.imshow('Video Feed', frame)

#         key = cv2.waitKey(1)
#         if key == ord('q'):
#             break
        
#         elif key == ord('r'):
#             cv2.imwrite('vid.mp4',out)

#         elif key == ord('c'):
#             cv2.imwrite('photo.jpg', frame)
#     else:
#         break

# # Release everything
# cap.release()
# out.release()
# cv2.destroyAllWindows()

import cv2


# Define the codec and create VideoCapture object
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

# Initialize variables
out = None
is_recording = False
frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

while True:
    ret, frame = cap.read()
    if ret:
        # Display the frame
        cv2.imshow('Video Feed', frame)

        # If recording, write the frame
        if is_recording and out is not None:
            out.write(frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        elif key == ord('r'):
            if not is_recording:
                # Start recording
                is_recording = True
                out = cv2.VideoWriter('output.mp4', fourcc, 30.0, frame_size)
                print("Recording started")
            else:
                # Stop recording
                is_recording = False
                out.release()
                out = None
                print("Recording stopped and saved as output.mp4")
        elif key == ord('c'):
            cv2.imwrite('photo.jpg', frame)
            print("Photo saved as photo.jpg")
    else:
        break

# Release everything
cap.release()
if out is not None:
    out.release()
cv2.destroyAllWindows()
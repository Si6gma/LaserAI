import cv2
import time

# Load the Haar cascade file
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Open the webcam
cap0 = cv2.VideoCapture(1)

lock_on = False
start_time = None

while True:
    # Read frames from the webcam
    ret0, frame0 = cap0.read()

    # Check if the frames were read correctly
    if not ret0:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Flip the frame horizontally
    frame0 = cv2.flip(frame0, 1)

    # Convert the frames to grayscale
    gray0 = cv2.cvtColor(frame0, cv2.COLOR_BGR2GRAY)

    # Perform face detection
    faces0 = face_cascade.detectMultiScale(gray0, 1.1, 4)

    # Draw rectangle around the faces
    for (x, y, w, h) in faces0:
        if lock_on:
            cv2.rectangle(frame0, (x, y), (x+w, y+h), (0, 0, 255), 2)
        else:
            cv2.rectangle(frame0, (x, y), (x+w, y+h), (0, 255, 0), 2)
            if start_time is None:
                start_time = time.time()
            elif time.time() - start_time > 3:
                lock_on = True

    # Display the resulting frames
    cv2.imshow('Webcam', frame0)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Reset lock-on and timer if no faces are detected
    if len(faces0) == 0:
        lock_on = False
        start_time = None

# Release the webcam and destroy all windows
cap0.release()
cv2.destroyAllWindows()

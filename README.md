# LaserTurret

**Work In Progress**

This project uses OpenCV to detect faces in a webcam feed, and two servos(motors) controlled by an Arduino to move a laser pointer to follow the detected face.

_Basically it points a laser into someone's eye_

## Coordination System (WIP)

The two servos control the pitch (x-axis), and yaw (y-axis)

Using arctan (tan inverse), we can figure out the two angles `α - pitch, θ - yaw` to control the laser.

The laser is at the origin for all the diagrams below:
![Coordination Plan](/assets/Coordination%20Plan.png)

`center_x` and `center_y` in `facialRecog.py` are the x and y coordinates

`Z coordinate` is the distance between the object and the laser, which is not measurable due to technical limitations, therefore will require manual calibration beforehand.

## Components

- A webcam for capturing video feed.
- An Arduino board for controlling the servos.
- Two servos for moving the laser pointer in two axes.
- A laser pointer.

## Software Dependencies

- Python(3)
- OpenCV Python library
- PySerial library for Python-Arduino communication
- Arduino IDE

## How it works (programmer edition)

1. The Python script uses _OpenCV_ to capture video from the webcam and detect faces in each frame.
2. The coordinates of the detected face are transformed _(using arctan shown in the coordination img)_ from the webcam frame's coordinate system to the servo's angles.
3. The transformed angles are sent to the Arduino via serial communication _(Pyserial)_.
4. The Arduino moves the servos to point the laser at the received angles.

## How it works (non-programmer edition)

1. Camera take location of face
2. It send to motors
3. Motors aim at target
4. Laser go brrrr

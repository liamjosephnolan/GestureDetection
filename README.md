# GestureDetection
Controlling arduino with gesture recognition

In order to control 

## Python
For Python I am using using cv2 and google's mediapipe library to read a webcam image and then process hand element landmarks onto this image. I then use these landmark elements to determine if the gesture is a thumb's up or down. According to this gesture I write a command to arduino's serial monitor.

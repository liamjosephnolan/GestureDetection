# GestureDetection
Controlling arduino with gesture recognition

I wrote this project for fun in order to pratice image processing and serial commication. I wanted to control an arduino using hand gestures and a webcam. In order to do so there were two seperate pieces of software I wrote. 

## Python
For Python I am using using cv2 and google's mediapipe library to read a webcam image and then process hand element landmarks onto this image. I then use these landmark elements to determine if the gesture is a thumb's up or down. According to this gesture I write a command to arduino's serial monitor.

## C
In C I simply read the command sent to the serial monitor and toggle the internal LED on the adruino accordingly. While not the most exciting application I am hoping to do more exciting projects with this in the future

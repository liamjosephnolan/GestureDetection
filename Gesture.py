import mediapipe as mp
import serial
import cv2


port = 'COM11' #Set COM port

baud_rate = 9600 # Set serial monitor rate (Usually 9600)
try:
    #Try connecting to arduino with the serial.serial command, using baud_rate and port
    arduino = serial.Serial(port=port, baudrate=baud_rate, timeout=.1)
    print(f"Successfully connected to {port} at {baud_rate} baud.")
except Exception as e:
    # Print if unsucessful
    print(f"Error: {e}")

# Open video capture element (I think)
cap = cv2.VideoCapture(0)

#Use media pipe to initalize hands
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

with mpHands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
        while cap.isOpened():
            success, img = cap.read()
            image = img.copy()
            if not success:
                print("Ignoring empty camera frame.")
                continue
            image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
            image.flags.writeable = False #not really sure what this line is doing but it makes the code run smoothly
            results = hands.process(image) # this is the line doing the hand processing
            try:

                Wrist_y = (results.multi_hand_landmarks[-1].landmark[0].y)*img.shape[0]
                Thumb_y = (results.multi_hand_landmarks[-1].landmark[4].y)*img.shape[0]
                # print(Wrist_y)
                # print(Thumb_y)

                if Thumb_y < Wrist_y:
                    print("Thumbs Up")
                    data_to_send = "1"
                    arduino.write(data_to_send.encode('utf-8'))

                if Thumb_y > Wrist_y:
                    print("Thumbs Down")
                    data_to_send = "0"
                    arduino.write(data_to_send.encode('utf-8'))

            except:
                pass


arduino.close()
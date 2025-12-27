import cv2
import pyfirmata
import numpy as np
import time
from pyfirmata import util

# ---------------- Camera ----------------
cap = cv2.VideoCapture(0)
ws, hs = 1280, 720
cap.set(3, ws)
cap.set(4, hs)

if not cap.isOpened():
    print("Camera couldn't Access!!!")
    exit()

# ---------------- Arduino ----------------
port = "COM11"
board = pyfirmata.Arduino(port)

it = util.Iterator(board)
it.start()
time.sleep(2)

servo_pinX = board.get_pin('d:9:s')
servo_pinY = board.get_pin('d:10:s')
led = board.get_pin('d:6:o')      # 🔴 LED PIN

# Initial servo position
servoPos = [90, 90]
servo_pinX.write(90)
servo_pinY.write(90)
led.write(0)                      # 🔴 LED OFF initially

# ---------------- Face Detector ----------------
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# ---------------- Main Loop ----------------
while True:
    success, img = cap.read()
    if not success:
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) > 0:
        # 🔴 FACE DETECTED → LED ON
        led.write(1)

        x, y, w, h = faces[0]
        fx = x + w // 2
        fy = y + h // 2

        servoX = np.interp(fx, [0, ws], [180, 0])
        servoY = np.interp(fy, [0, hs], [180, 0])

        servoX = np.clip(servoX, 0, 180)
        servoY = np.clip(servoY, 0, 180)

        servoPos[0] = servoX
        servoPos[1] = servoY

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.circle(img, (fx, fy), 15, (0, 0, 255), cv2.FILLED)
        cv2.putText(img, "TARGET LOCKED", (850, 50),
                    cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    else:
        # ⚫ NO FACE → LED OFF
        led.write(0)

        cv2.putText(img, "NO TARGET", (880, 50),
                    cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)

    # Move servos
    servo_pinX.write(servoPos[0])
    servo_pinY.write(servoPos[1])

    cv2.imshow("Face Tracking", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()







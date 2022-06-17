import math
import cv2
from numpy import (interp, uint8, array)
from time import sleep
from mediapipe.python.solutions.hands import Hands
import ctypes
import imutils
import requests

width_display, height_display = 1366, 768
width_cam, height_cam = 640, 480

url = 'http://25.174.141.66:8080/shot.jpg'

smoothen = 6
previous_x, previous_y = 0, 0
current_x, current_y = 0, 0

hands = Hands()

def get_image():            
    img_reqs = requests.get(url)
    img_arr = array(bytearray(img_reqs.content), dtype=uint8)
    img_deco = cv2.imdecode(img_arr, -1)
    img_flip = cv2.flip(img_deco, 0)
    return imutils.resize(img_flip, width=width_cam, height=height_cam)

def trackHand():
    while True:
        global previous_x, previous_y, current_x, current_y

        img = get_image()
        results = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

        handType = "Right"
        h, w, c = img.shape
        my_lm_list = []

        if results.multi_hand_landmarks:
            for handType, handLms in zip(results.multi_handedness, results.multi_hand_landmarks):
                for lm in handLms.landmark:
                    px, py = int(lm.x * w), int(lm.y * h)
                    my_lm_list.append([px, py])
        
        if my_lm_list:
            x1, y1 = my_lm_list[8]
            x2, y2 = my_lm_list[12]
            tipIds = [4, 8, 12, 16, 20]
            finger_up = []

            if handType == "Right":
                if my_lm_list[tipIds[0]][0] > my_lm_list[tipIds[0] - 1][0]:
                    finger_up.append(1)
                else:
                    finger_up.append(0)
            else:
                if my_lm_list[tipIds[0]][0] < my_lm_list[tipIds[0] - 1][0]:
                    finger_up.append(1)
                else:
                    finger_up.append(0)
            
            for f in range(1, 5):
                if my_lm_list[tipIds[f]][1] < my_lm_list[tipIds[f] - 2][1]:
                    finger_up.append(1)
                else:
                    finger_up.append(0)
            
            frameRX, frameRY = 180, 180
            width_frame, height_frame = width_cam - frameRX, height_cam - frameRY

            if finger_up[1] == 1 and finger_up[2] == 0:

                x3 = interp(x1, (frameRX, width_frame), (0, width_display))
                y3 = interp(y1, (frameRY, height_frame), (0, height_display))

                current_x = int(previous_x + (x3 - previous_x) / smoothen)
                current_y = int(previous_y + (y3 - previous_y) / smoothen)

                ctypes.windll.user32.SetCursorPos(current_x, current_y)
                previous_x, previous_y = current_x, current_y

            if finger_up[1] == 1 and finger_up[2] == 1:
                length = math.hypot(x2 - x1, y2 - y1)

                if length < 30:
                    ctypes.windll.user32.mouse_event(0x0002)
                    ctypes.windll.user32.mouse_event(0x0004)
                    sleep(0.3)
        
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    
    cv2.destroyAllWindows()
    return 'exit code 1'

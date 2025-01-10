import base_keys
from base_component import BaseComponent
import cv2
import time

from Processors.sign_detector.HandTrackingModule import handDetector as htm

from Utilities import logging_utility

_logger = logging_utility.setup_logger(__name__)

class HandSignDetector(BaseComponent):

    def __init__(self, name, cam_width=640, cam_height=480, detection_confidence=0):
        super().__init__(name)

        self.cam_width = cam_width
        self.cam_height = cam_height
        self.detection_confidence = detection_confidence

        # Initialize the hand detector
        self.detector = htm(detectionCon=self.detection_confidence)
        self.last_detection_time = 0  # Store last detection time
        self.last_sign = None  # Store the last detected sign
        self.x_coord = 55
        self.detected_signs = []  # List to store previously detected signs and their positions


    def detect_sign(self, pos_list):
        """Detect the hand sign based on finger positions."""
        fingers = []

        finger_dip = [6, 10, 14, 18]
        finger_pip = [7, 11, 15, 19]
        finger_tip = [8, 12, 16, 20]

        for id in range(4):
            if pos_list[finger_tip[id]][1] + 25 < pos_list[finger_dip[id]][1] and pos_list[16][2] < pos_list[20][2]:
                fingers.append(0.25)
            elif pos_list[finger_tip[id]][2] > pos_list[finger_dip[id]][2]:
                fingers.append(0)
            elif pos_list[finger_tip[id]][2] < pos_list[finger_pip[id]][2]:
                fingers.append(1)
            elif pos_list[finger_tip[id]][1] > pos_list[finger_pip[id]][1] and pos_list[finger_tip[id]][1] > pos_list[finger_dip[id]][1]:
                fingers.append(0.5)
        
        if len(pos_list) >=21 and len(fingers) >=4:
        # Detect specific signs (example: A, B, C)
            if(pos_list[3][2] > pos_list[4][2]) and (pos_list[3][1] > pos_list[6][1])and (pos_list[4][2] < pos_list[6][2]) and fingers.count(0) == 4:
                return "A"
                
            elif(pos_list[3][1] > pos_list[4][1]) and fingers.count(1) == 4:
                return "B"
            
            elif(pos_list[3][1] > pos_list[6][1]) and fingers.count(0.5) >= 1 and (pos_list[4][2]> pos_list[8][2]):
                return "C"
                
            elif(fingers[0]==1) and fingers.count(0) == 3 and (pos_list[3][1] > pos_list[4][1]):
                return "D"
            
            elif (pos_list[3][1] < pos_list[6][1]) and fingers.count(0) == 4 and pos_list[12][2]<pos_list[4][2]:
                return "E"

            elif (fingers.count(1) == 3) and (fingers[0]==0) and (pos_list[3][2] > pos_list[4][2]):
                return "F"

            elif(fingers[0]==0.25) and fingers.count(0) == 3:
                return "G"

            elif(fingers[0]==0.25) and(fingers[1]==0.25) and fingers.count(0) == 2:
                return "H"
            
            elif (pos_list[4][1] < pos_list[6][1]) and fingers.count(0) == 3:
                if (len(fingers)==4 and fingers[3] == 1):
                    return "I"
            
            elif (pos_list[4][1] < pos_list[6][1] and pos_list[4][1] > pos_list[10][1] and fingers.count(1) == 2):
                return "K"
                
            elif(fingers[0]==1) and fingers.count(0) == 3 and (pos_list[3][1] < pos_list[4][1]):
                return "L"
            
            elif (pos_list[4][1] < pos_list[16][1]) and fingers.count(0) == 4:
                return "M"
            
            elif (pos_list[4][1] < pos_list[12][1]) and fingers.count(0) == 4:
                return "N"
                
            elif(pos_list[3][1] > pos_list[6][1]) and (pos_list[3][2] < pos_list[6][2]) and fingers.count(0.5) >= 1:
                return "O"
            
            elif (pos_list[4][1] > pos_list[12][1]) and pos_list[4][2]<pos_list[6][2] and fingers.count(0) == 4:
                return "T"

            elif (pos_list[4][1] > pos_list[12][1]) and pos_list[4][2]<pos_list[12][2] and fingers.count(0) == 4:
                return "S"

            
            elif(pos_list[4][2] < pos_list[8][2]) and (pos_list[4][2] < pos_list[12][2]) and (pos_list[4][2] < pos_list[16][2]) and (pos_list[4][2] < pos_list[20][2]):
                return "O"
            
            elif(fingers[2] == 0)  and (pos_list[4][2] < pos_list[12][2]) and (pos_list[4][2] > pos_list[6][2]):
                if (len(fingers)==4 and fingers[3] == 0):
                    return "P"
            
            elif(fingers[1] == 0) and (fingers[2] == 0) and (fingers[3] == 0) and (pos_list[8][2] > pos_list[5][2]) and (pos_list[4][2] < pos_list[1][2]):
                return "Q"
            
            # elif(pos_list[10][2] < pos_list[8][2] and fingers.count(0) == 4 and pos_list[4][2] > pos_list[14][2]):
            #     return "Q" 
                
            elif(pos_list[8][1] < pos_list[12][1]) and (fingers.count(1) == 2) and (pos_list[9][1] > pos_list[4][1]):
                return "R"
                
            elif (pos_list[3][1] < pos_list[6][1]) and fingers.count(0) == 4:
                return "S"
                
            elif (pos_list[4][1] < pos_list[6][1] and pos_list[4][1] < pos_list[10][1] and fingers.count(1) == 2 and pos_list[3][2] > pos_list[4][2] and (pos_list[8][1] - pos_list[11][1]) <= 50):
                return "U"
                
            elif (pos_list[4][1] < pos_list[6][1] and pos_list[4][1] < pos_list[10][1] and fingers.count(1) == 2 and pos_list[3][2] > pos_list[4][2]):
                return "V"
            
            elif (pos_list[4][1] < pos_list[6][1] and pos_list[4][1] < pos_list[10][1] and fingers.count(1) == 3):
                return "W"
            
            elif (fingers[0] == 0.5 and fingers.count(0) == 3 and pos_list[4][1] > pos_list[6][1]):
                return "X"
            
            elif(fingers.count(0) == 3) and (pos_list[3][1] < pos_list[4][1]):
                if (len(fingers)==4 and fingers[3] == 1):
                    return "Y"

        return ".."

    def run(self, raw_data):
        """
        Process the raw data to detect hand signs and send processed data to the next component.
        """
        current_time = time.time()  # Get the current timestamp
        frame = raw_data[base_keys.CAMERA_FRAME]

        # Find hands and their positions
        annotated_frame = self.detector.findHands(frame)

        if current_time - self.last_detection_time >= 1:  # Check if 3 seconds have passed
            self.last_detection_time = current_time  # Update the last detection time

            pos_list = self.detector.findPosition(annotated_frame, draw=False)

            if pos_list:
                new_sign = self.detect_sign(pos_list)
            else:
                new_sign = ".."
            
            if new_sign != self.last_sign:
                if self.x_coord >= (5*100) + 55:
                    self.x_coord = 55
                    self.detected_signs.clear()  # Clear the previous signs

                self.last_sign = new_sign  # Update the stored sign
                self.detected_signs.append((self.last_sign, self.x_coord))  # Store the new sign and its position
                self.x_coord += 30  # Increment the position for the next sign
        
        # Annotate the frame with all detected signs and their positions
        opacity = 0.5
        overlay = annotated_frame.copy()
        cv2.rectangle(overlay, (55, 375), (555, 400), (0, 0, 0), thickness=cv2.FILLED)

        for sign, x in self.detected_signs:
            cv2.addWeighted(overlay, opacity, annotated_frame, 1 - opacity, 0, annotated_frame)
            cv2.putText(annotated_frame, str(sign), (x, 400), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
            overlay = annotated_frame.copy()
        print(self.detected_signs)

        

        # Continue sending the frame regardless of gesture detection
        super().send_to_component(hand_frame=annotated_frame, base_data=raw_data)
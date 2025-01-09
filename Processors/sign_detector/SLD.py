import base_keys
from base_component import BaseComponent
import cv2

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

        # Detect specific signs (example: A, B, C)
        if pos_list[3][2] > pos_list[4][2] and pos_list[3][1] > pos_list[6][1] and pos_list[4][2] < pos_list[6][2] and fingers.count(0) == 4:
            return "A"
        elif pos_list[3][1] > pos_list[4][1] and fingers.count(1) == 4:
            return "B"
        elif pos_list[3][1] > pos_list[6][1] and fingers.count(0.5) >= 1 and pos_list[4][2] > pos_list[8][2]:
            return "C"

        return "..."

    def run(self, raw_data):
        """
        Process the raw data to detect hand signs and send processed data to the next component.
        If raw_data is None, it will read from the camera feed.
        """
        super().set_component_status(base_keys.COMPONENT_IS_RUNNING_STATUS)


        frame = raw_data[base_keys.CAMERA_FRAME]

        # Find hands and their positions
        annotated_frame = self.detector.findHands(frame)

        pos_list = self.detector.findPosition(annotated_frame, draw=False)

        if pos_list:
            last_sign = self.detect_sign(pos_list)
        else:
            last_sign = "..."

        print(pos_list)

        # Annotate the frame with the detected sign
        cv2.putText(annotated_frame, str(last_sign), (55, 400), cv2.FONT_HERSHEY_COMPLEX, 5, (255, 255, 255), 15)
        
        super().send_to_component(hand_frame=annotated_frame,
                                  base_data=raw_data)
       
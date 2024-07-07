import cv2
import numpy as np
import mediapipe as mp
import argparse
import itertools
from train.model_landmark import LandMarkModel
from model.eval_dataset import EvalDataset
from torch.utils.data import Dataset, DataLoader
import torch

# import time
import copy
# from utils import CvFpsCalc

class runWebCam():
    def get_args(self):
        parser = argparse.ArgumentParser()

        parser.add_argument("--device", type=int, default=0)
        parser.add_argument("--width", help='cap width', type=int, default=960)
        parser.add_argument("--height", help='cap height', type=int, default=540)

        parser.add_argument('--use_static_image_mode', action='store_true')
        parser.add_argument("--min_detection_confidence",
                            help='min_detection_confidence',
                            type=float,
                            default=0.7)
        parser.add_argument("--min_tracking_confidence",
                            help='min_tracking_confidence',
                            type=int,
                            default=0.5)
        parser.add_argument("--model_path",
                            help='model_path',
                            type=str,
                            default='model/save/model.pth')

        args = parser.parse_args()

        return args
    

    def calc_landmark_list(self, image, landmarks):
        image_width, image_height = image.shape[1], image.shape[0]

        landmark_point = []

        # Keypoint
        for _, landmark in enumerate(landmarks.landmark):
            landmark_x = min(int(landmark.x * image_width), image_width - 1)
            landmark_y = min(int(landmark.y * image_height), image_height - 1)
            # landmark_z = landmark.z

            landmark_point.append([landmark_x, landmark_y])

        return landmark_point
    
    
    def pre_process_landmark(self,landmark_list):
        temp_landmark_list = copy.deepcopy(landmark_list)

        # Convert to relative coordinates
        base_x, base_y = 0, 0
        for index, landmark_point in enumerate(temp_landmark_list):
            if index == 0:
                base_x, base_y = landmark_point[0], landmark_point[1]

            temp_landmark_list[index][0] = temp_landmark_list[index][0] - base_x
            temp_landmark_list[index][1] = temp_landmark_list[index][1] - base_y

        # Convert to a one-dimensional list
        temp_landmark_list = list(
            itertools.chain.from_iterable(temp_landmark_list))

        # Normalization
        max_value = max(list(map(abs, temp_landmark_list)))

        def normalize_(n):
            return n / max_value
        
        temp_landmark_list = list(map(normalize_, temp_landmark_list))

        return temp_landmark_list
    
    def recogniseGesture(self, pre_processed_landmark_list): 
        # Import model 
        args = self.get_args()
        model = LandMarkModel(input_size=42,output_size=6)
        model_path = args.model_path
        model_load = torch.load(model_path)
        model.load_state_dict(model_load)
        model.eval()
        
        # Making test frames from camera into test dataset
        test_dataset = EvalDataset(pre_processed_landmark_list)
        test_data = DataLoader(test_dataset, shuffle=False)

        # Applying model to the test data
        gesture = model(test_data)
        print(gesture)
        return gesture

    def startVideo(self):
        # Argument parsing #################################################################
        args = self.get_args()

        # cap_device = args.device
        # cap_width = args.width
        # cap_height = args.height

        use_static_image_mode = args.use_static_image_mode
        min_detection_confidence = args.min_detection_confidence
        min_tracking_confidence = args.min_tracking_confidence

        # use_brect = True

        # Model load #############################################################
        mp_hands = mp.solutions.hands
        hands = mp_hands.Hands(
            static_image_mode=use_static_image_mode,
            max_num_hands=1,
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence,
        )

        # Initialize the webcam
        cap = cv2.VideoCapture(0)

        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()
            
            frame = cv2.flip(frame, 1)  # Mirror display
            debug_image = copy.deepcopy(frame)

            # Apply model
            results = hands.process(frame)

            if results.multi_hand_landmarks is not None:
                for hand_landmarks, handedness in zip(results.multi_hand_landmarks,
                                                    results.multi_handedness):
                    landmark_list = self.calc_landmark_list(debug_image, hand_landmarks)
                    # print(landmark_list)

                    # Obtain normalized coordinates
                    pre_processed_landmark_list = self.pre_process_landmark(landmark_list)
                    
                    # Predict the gesture
                    gesture = self.recogniseGesture(pre_processed_landmark_list=pre_processed_landmark_list)
                                                
            # If frame is read correctly ret is True
            if not ret:
                print("Failed to grab frame")
                break
            
            # Display the resulting frame
            cv2.imshow('Webcam', frame)
            
            # Break the loop on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            # time.sleep(1)

        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()

    
if __name__ == "__main__":
    webcam = runWebCam()
    webcam.startVideo()
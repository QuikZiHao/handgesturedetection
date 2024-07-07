import numpy as np
import argparse
from train.model_landmark import LandMarkModel
from model.eval_dataset import EvalDataset
from torch.utils.data import Dataset, DataLoader
import torch
import cv2
from utils.process import Proceed
from train.model_process import load_model
from utils.webcam import WebCam
import utils.magicfunction as MagicFunction
import time

# import time
import copy
# from utils import CvFpsCalc

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--func_amt",type=int,default=6)
    parser.add_argument("--remember_step",type=int,default=100)
    parser.add_argument("--proceed_score",type=int,default=10)
    parser.add_argument("--width", help='cap width', type=int, default=960)
    parser.add_argument("--height", help='cap height', type=int, default=540)
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

def main():
    args = get_args()
    model = LandMarkModel(42, output_size=args.func_amt)
    model = load_model(model=model, file_path=args.model_path)
    model.eval()
    exec_unit = Proceed(
        func_amt=args.func_amt,
        remember_stamp=args.remember_step,
        proceed_score=args.proceed_score
        )
    flag = True
    cooldown = 0
    cam = WebCam(min_detection_confidence=args.min_detection_confidence,
                 min_tracking_confidence=args.min_tracking_confidence)
    func_hash = {
        0: MagicFunction.play_pause_track,
        1: MagicFunction.previous_track,
        2: MagicFunction.next_track,
        3: MagicFunction.do_screenshot,
        4: MagicFunction.do_paste,
        5: MagicFunction.do_copy,
        -1: None
    }
    
    while True:
        kwargs = cam.run()
        cv2.imshow('Webcam', kwargs["frame"])
        # Break the loop on 'esc' key press
        key = cv2.waitKey(10)
        if key == 27:  # ESC
            break
        if len(kwargs["landmark"]) == 0:
            continue
        temp = model.get_score(kwargs["landmark"])
        max_idxs = torch.argmax(temp, dim=1)
        for i in range(len(max_idxs)):
            score = temp[i][max_idxs[i]]
            idx = int(max_idxs[i].item())
            process = func_hash[exec_unit.step(idx, score)]
            print("score", max(exec_unit.conf_array), "index", idx)
            if process == None:
                continue
            process()

        # time.sleep(1)
    cam.cam.release()
    cv2.destroyAllWindows()

     
if __name__ == "__main__":
    main()
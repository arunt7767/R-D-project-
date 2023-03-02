import cv2
import torch
import numpy as np
import pyautogui

model = torch.hub.load('ultralytics/yolov5', 'yolov5m6')
def capture_video():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        yield frame

def detect_objects(frame):
    results = model(frame)
    return results.pred

def click_picture_and_save(location):
    pyautogui.click()
    pyautogui.screenshot(location)

def main():
    for frame in capture_video():
        objects = detect_objects(frame)
        for obj in objects:
            if obj.names[0] == "specific_object_name":
                click_picture_and_save("/Users/arunsinghthakur/screenshot.png")

if __name__ == '__main__':
    main()


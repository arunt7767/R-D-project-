import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2

model = torch.hub.load('ultralytics/yolov5', 'yolov5m6')
#model = torch.hub.load('ultralytics/yolov5', 'custom', 'yolov5m-seg.pt') 
cap = cv2.VideoCapture(0 )
while cap.isOpened():
    ret, frame = cap.read()
    
    # Make detections 
    results = model(frame)
    
    cv2.imshow('YOLO', np.squeeze(results.render()))
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
def click_picture_and_save(location):
    pyautogui.click()
    pyautogui.screenshot(location)
cap.release()
cv2.destroyAllWindows()
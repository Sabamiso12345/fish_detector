from fastapi import FastAPI
from PIL import Image
from ultralytics import YOLO
import numpy as np
import matplotlib.pyplot as plt



#load a pretrained model
model = YOLO("/Users/Yoshikage-Goto/Desktop/yolov8_1/models/last.pt")

source = '/content/penguin.jpeg'
results = model(source) 

for r in results:
    im_array = r.plot()  # plot a BGR numpy array of predictions
    im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
    





import cv2
import matplotlib as matplotlib
import pandas
import torch
from PIL import Image
import requests
import yaml
from matplotlib import pyplot as plt
from tqdm import tqdm
import torchvision
import matplotlib.pyplot as plt
import seaborn as sn

# model = torch.hub.load('ultralytics/yolov5', 'custom', path='trained_model/model4.3.pt')
model = './trained_model/state_dict_model4.3.pt'
model.load_state_dict(torch.load('./trained_model/state_dict_model4.3.pt'))
im1 = Image.open('./detecto/imgs/onion/test/onion_2.jpg')
results = model(im1)
results.print()
results.show()
# print(results.xyxy[0])
# print(results.pandas().xyxy[0])
xmin = results.pandas().xyxy[0].xmin[0]
ymin = results.pandas().xyxy[0].ymin[0]
xmax = results.pandas().xyxy[0].xmax[0]
ymax = results.pandas().xyxy[0].ymax[0]
confidence = results.pandas().xyxy[0].confidence[0]
name = results.pandas().xyxy[0].name[0]
print(f'xmin = {xmin}, ymin = {ymin}, xmax = {xmax}, ymax = {ymax}, \nconfidence = {round(confidence * 100, 2)}%, '
      f'name = {name}')


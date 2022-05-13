import kwargs as kwargs
from certifi.__main__ import args

from modules import *

import torch
from PIL import Image

import torch as torch
from torch import nn, optim
import torch.nn.functional as F
import torchvision.transforms as transforms

import torch
import torch.nn as nn
import torch.nn.functional as F

# ANNA TESTAR
# class TheModelClass(nn.Module):
#     def __init__(self):
#         super().__init__()
#         self.conv1 = nn.Conv2d(1, 6, 5)
#         # we use the maxpool multiple times, but define it once
#         self.pool = nn.MaxPool2d(2, 2)
#         # in_channels = 6 because self.conv1 output 6 channel
#         self.conv2 = nn.Conv2d(6, 16, 5)
#         # 5*5 comes from the dimension of the last convnet layer
#         self.fc1 = nn.Linear(16 * 157 * 117, 256) # You didnt provide the numbers here but i did calculate the in channels based off the prev layer
#         self.fc2 = nn.Linear(256, 10)
#         self.fc3 = nn.Linear(10, 2)
#
#     def forward(self, x):
#         x = self.conv1(x)
#         print('Conv1 Shape: {}'.format(x.shape))
#         x = self.pool(F.relu(x))
#         print('Pool1 Shape: {}'.format(x.shape))
#         x = self.conv2(x)
#         print('Conv2 Shape: {}'.format(x.shape))
#         x = self.pool(F.relu(x))
#         print('Pool2 Shape: {}'.format(x.shape))
#         x = x.view(-1, 16 * 157 * 117)
#         print('Flatten Shape: {}'.format(x.shape))
#         x = F.relu(self.fc1(x))
#         x = F.relu(self.fc2(x))
#         x = self.fc3(x)  # no activation on final layer
#         return x

# Define model
class TheModelClass(nn.Module):
    def __init__(self):
        super(TheModelClass, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16 * 5 * 5)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x


# Initialize model
model = TheModelClass()
# model(torch.randn(1, 1, 640, 480))

# model = torch.hub.load('ultralytics/yolov5', 'custom', path='trained_model/model4.3.pt')

state_dict = torch.load('./trained_model/state_dict_model4.3.pt')
model.load_state_dict(state_dict)
model.eval()

im1 = Image.open('./detecto/imgs/onion/test/onion_2.jpg')
transform = transforms.Compose([transforms.PILToTensor()])

img_tensor = transform(im1)
img_tensor = img_tensor.float()
shape = img_tensor.shape

# print(img_tensor)

# TODO - nej joakim
# call model with image as a tensor
# Check how yolov did it (dig deep in the yolov code)
results = model(img_tensor)
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


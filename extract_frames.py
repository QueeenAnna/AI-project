from kivy.app import App
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.clock import Clock
import numpy as np
import os
import cv2
import torch
import cv2
import matplotlib as matplotlib
import pandas
import torch

import requests
import yaml
from matplotlib import pyplot as plt
from tqdm import tqdm
import torchvision
import matplotlib.pyplot as plt
import seaborn as sn

vid = cv2.VideoCapture(0)


def generate_texture():

    # numpy array
    # img = np.random.randint(0, 256, size=(500, 500, 3), dtype=np.uint8)

    # Hej, jag är dirigenten!
    _, img = vid.read()
    # Hepp, nu har jag en bild från kameran

    # Den skickar jag till modellen för klassificering
    # => Skick
    get_coordinates_and_labels(img)

    # os.system(f"python yolov5.0/detect.py --source {img} --weights ./trained_model/model4.2.pt")
    #
    #     # Tillbaka från modellen får jag nu en lista på alla objekt som den hittade
    #     # och var rektanglarna skall ritas ut på bilder
    #
    #     # Nu ritar jag ut rektanglarna
    #     # cv2.circle(img, (img.shape[1] // 2, img.shape[0] // 2), 100, 255, -1)
    #
    #     # Nu skall skall jag få över bilden till kivy. För att det skall funka
    # måste bilddatat vara i enn texture-format
    # data = img.tobytes()

    # texture
    # texture = Texture.create(size=(img.shape[1], img.shape[0]), colorfmt="bgr")
    # texture.blit_buffer(data, bufferfmt="ubyte", colorfmt="bgr")

    # Vi returnerar vår texture så att kivy kan plocka upp den och visa den på skärmen
    # return texture


def get_coordinates_and_labels(img):
    from PIL import Image
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='trained_model/model4.3.pt')

    im1 = Image.open(img)
    # im1 = Image.open('./detecto/imgs/onion/test/onion_2.jpg')
    results = model(im1)
    xmin = results.pandas().xyxy[0].xmin[0]
    ymin = results.pandas().xyxy[0].ymin[0]
    xmax = results.pandas().xyxy[0].xmax[0]
    ymax = results.pandas().xyxy[0].ymax[0]
    confidence = results.pandas().xyxy[0].confidence[0]
    name = results.pandas().xyxy[0].name[0]
    # print(f'xmin = {xmin}, ymin = {ymin}, xmax = {xmax}, ymax = {ymax}, \nconfidence = {round(confidence * 100, 2)}%, '
          # f'name = {name}')

    return xmin, ymin, xmax, ymax, confidence, name


def update_image(dt):
    """Replace texture in existing image."""

    image.texture = generate_texture()


# --- main ---

# empty image at start
image = Image()


class MyPaintApp(App):
    def build(self):
        return image


# run function every 0.25 s
Clock.schedule_interval(update_image, 0.025)

if __name__ == '__main__':
    MyPaintApp().run()


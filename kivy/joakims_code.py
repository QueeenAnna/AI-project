from kivy.app import App
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.clock import Clock
import numpy as np
import cv2
import os

vid = cv2.VideoCapture(0)
# --- functions ---

def generate_texture():
    # numpy array
    # img = np.random.randint(0, 256, size=(500, 500, 3), dtype=np.uint8)

    # Hej, jag är dirigenten!
    _, img = vid.read()
    # Hepp, nu har jag en bild från kameran

    # Den skickar jag till modellen för klassificering
    # => Skick

    # Tillbaka från modellen får jag nu en lista på alla objekt som den hittade
    # och var rektanglarna skall ritas ut på bilder

    # Nu ritar jag ut rektanglarna
    cv2.circle(img, (img.shape[1] // 2, img.shape[0] // 2), 100, 255, -1)

    # Nu skall skall jag få över bilden till kivy. För att det skall funka
    # måste bilddatat vara i enn texture-format
    data = img.tobytes()

    # texture
    texture = Texture.create(size=(img.shape[1], img.shape[0]), colorfmt="bgr")
    texture.blit_buffer(data, bufferfmt="ubyte", colorfmt="bgr")

    # Vi returnerar vår texture så att kivy kan plocka upp den och visa den på skärmen

    return texture


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

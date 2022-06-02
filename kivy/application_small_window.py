import os

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.clock import Clock
import cv2
import pytesseract
from kivymd.uix.label import MDLabel
# from PIL import Image


class MainApp(MDApp):

    def build(self):
        layout = MDBoxLayout(orientation='vertical')
        self.image = Image()
        self.label = MDLabel()
        layout.add_widget(self.image)
        layout.add_widget(self.label)
        self.save_img_button = MDRaisedButton(
            text="Start Scanning",
            pos_hint={'center_x': .5, 'center_y': .5},
            size_hint=(None, None))
        self.save_img_button.bind(on_press=self.take_picture)
        layout.add_widget(self.save_img_button)
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.load_video, 1.0/30.0)
        return layout

    def load_video(self, *args):
        ret, frame = self.capture.read()
        # Frame initialize
        self.image_frame = frame
        buffer = cv2.flip(frame, 0).tostring()
        texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
        self.image.texture = texture

    def take_picture(self, *args):
        os.system("python yolov5/detect.py --source 0 --weights yolov5/trained_model/best.pt --save-txt")


if __name__ == '__main__':
    MainApp().run()

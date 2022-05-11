from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import os
import time
Builder.load_string('''
<CameraClick>:
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (640, 640)
        play: False
    ToggleButton:
        text: 'Play'
        on_press: camera.play = not camera.play
        size_hint_y: None
        height: '48dp'
    Button:
        text: 'Run script'
        size_hint_y: None
        height: '48dp'
        on_press: root.capture()
''')


class CameraClick(BoxLayout):
    def capture(self):
        os.system(f"python yolov5/detect.py --source 0 --weights ./trained_model/best.pt --save-txt")


class TestCamera(App):

    def build(self):
        return CameraClick()


TestCamera().run()
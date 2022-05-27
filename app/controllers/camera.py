import os.path
import torch
import numpy as np
from time import time
import cv2


class Video(object):
    def __init__(self):
        self.video = cv2.VideoCapture(1)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        ret, frame = self.video.read()
        # Är det här vi ska få in frames
        ret, jpg = cv2.imencode('.jpg', frame)

        return jpg.tobytes()


class FoodDetection:

    def __init__(self, capture_index, model_name):

        self.capture_index = capture_index
        self.model = self.load_model('./' + model_name)
        self.classes = self.model.names
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        print("using device: ", self.device)

    def get_video_capture(self):
        return cv2.VideoCapture(self.capture_index)

    def load_model(self, model_name):
        if model_name:
            model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_name, force_reload=True)
        else:
            model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
        return model

    def score_frame(self, frame):
        self.model.to(self.device)
        frame = [frame]
        results = self.model(frame)
        labels, cord = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]
        # print(results.pandas().xyxy[0])

        return labels, cord

    def class_to_label(self, x):
        return self.classes[int(x)]

    def plot_boxes(self, results, frame):
        labels, cord = results
        n = len(labels)
        x_shape, y_shape = frame.shape[1], frame.shape[0]

        for i in range(n):
            row = cord[i]

            if row[4] >= 0.2:
                x1, y1, x2, y2 = int(row[0] * x_shape), int(row[1] * y_shape), int(row[2] * x_shape), int(
                    row[3] * y_shape)
                bgr = (0, 255, 0)
                cv2.rectangle(frame, (x1, y1), (x2, y2), bgr, 2)
                cv2.putText(frame, self.class_to_label(labels[i]), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.9, bgr, 2)

        return frame

    def get_frame(self):
        cap = self.get_video_capture()
        assert cap.isOpened()

        while True:

            ret, frame = cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                assert ret

                frame = cv2.resize(frame, (670, 470))
                start_time = time()
                results = self.score_frame(frame)
                frame = self.plot_boxes(results, frame)

                endtime = time()
                fps = 1 / np.round(endtime - start_time, 2)

                cv2.putText(frame, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                yield cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            else:
                yield cv2.imread('Testbild.png')
            # # cv2.imshow('foodapp', frame)
            # if cv2.waitKey(5) & 0xFF == 27:
            #     break
        # cap.release()


# detector = FoodDetection(capture_index=1, model_name='model_150_epoches.pt')
# detector()

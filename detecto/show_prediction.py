from detecto.core import Model
import cv2
from detecto.utils import read_image


def main():
    model = Model.load('gesture_model.pth', ['FingersCrossed', 'Hello', 'ThumbsDown', 'ThumbsUp'])

    img = cv2.imread('./images/test/image_name.jpg')
    img2 = read_image('./images/test/image_name.jpg')
    labels, boxes, scores = model.predict(img2)

    x1, y1, x2, y2 = boxes[0]
    cv2.rectangle(img, (int(x1), int(y1), int(x2), int(y2)), (0, 255, 0), 2)
    cv2.putText(img, labels[0], (int(x1), int(y1)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
    cv2.imshow('Result', img)

    cv2.waitKey(0)

    print()

if __name__ == '__main__':
    main()


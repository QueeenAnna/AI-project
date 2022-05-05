import cv2
import numpy as np


def main():
    img = cv2.imread("imgs/red_onion_original/red_onion_42.jpg")

    grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    kernel = np.ones((5, 5), np.uint8)

    cv2.namedWindow('parameters')
    cv2.resizeWindow('parameters', 640, 240)
    cv2.createTrackbar('threshold1', 'parameters', 150, 500, lambda x: 0)
    cv2.createTrackbar('threshold2', 'parameters', 255, 500, lambda x: 0)
    cv2.createTrackbar('blur', 'parameters', 1, 25, lambda x: 0)
    cv2.createTrackbar('dialate', 'parameters', 0, 7, lambda x: 0)
    cv2.createTrackbar('eroded', 'parameters', 0, 7, lambda x: 0)

    while True:
        threshold1 = cv2.getTrackbarPos('threshold1', 'parameters')
        threshold2 = cv2.getTrackbarPos('threshold2', 'parameters')
        blur = cv2.getTrackbarPos('blur', 'parameters')
        dialate = cv2.getTrackbarPos('dialate', 'parameters')
        eroded = cv2.getTrackbarPos('eroded', 'parameters')
        blur_img = cv2.GaussianBlur(grey_img, (5, 5), blur)
        img_canny = cv2.Canny(blur_img, threshold1, threshold2)
        dia_img = cv2.dilate(img_canny, kernel, iterations=dialate)
        eroded_img = cv2.erode(dia_img, kernel, iterations=eroded)
        cv2.imshow('image', eroded_img)
        cv2.waitKey(1)


if __name__ == '__main__':
    main()

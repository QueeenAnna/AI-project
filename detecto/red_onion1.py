import cv2
import numpy as np


def stack_images(scale, img_array):
    rows = len(img_array)
    cols = len(img_array[0])
    rows_available = isinstance(img_array[0], list)
    width = img_array[0][0].shape[1]
    height = img_array[0][0].shape[0]
    if rows_available:
        for x in range(0, rows):
            for y in range(0, cols):
                if img_array[x][y].shape[:2] == img_array[0][0].shape[:2]:
                    img_array[x][y] = cv2.resize(img_array[x][y], (0, 0), None, scale, scale)
                else:
                    img_array[x][y] = cv2.resize(img_array[x][y],
                                                 (img_array[0][0].shape[1], img_array[0][0].shape[0]),
                                                 None,
                                                 scale,
                                                 scale)
                if len(img_array[x][y].shape) == 2: img_array[x][y] = cv2.cvtColor(img_array[x][y], cv2.COLOR_GRAY2BGR)
        image_blank = np.zeros((height, width, 3), np.uint8)
        hor = [image_blank] * rows

        for x in range(0, rows):
            hor[x] = np.hstack(img_array[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if img_array[x].shape[:2] == img_array[0].shape[:2]:
                img_array[x] = cv2.resize(img_array[x], (0, 0), None, scale, scale)
            else:
                img_array[x] = cv2.resize(img_array[x],
                                          (img_array[0].shape[1], img_array[0].shape[0]),
                                          None,
                                          scale,
                                          scale)
            if len(img_array[x].shape) == 2:
                img_array[x] = cv2.cvtColor(img_array[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(img_array)
        ver = hor
    return ver


def get_contours(img, img_contour):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        area = cv2.contourArea(contour)
        cv2.drawContours(img_contour, contour, -1, (255, 0, 0), 3)
        arc_length = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, arc_length * 0.02, True)
        obj_corners = len(approx)
        x, y, w, h = cv2.boundingRect(approx)
        cv2.rectangle(img_contour, (x, y), (x + w, y + h), (0, 255, 0), 2)

        if obj_corners == 3:
            object_type = 'Triangle'
        elif obj_corners == 4:
            asp_ratio = w / float(h)
            if 0.98 < asp_ratio < 1.03:
                object_type = 'Square'
            else:
                object_type = 'Rectangle'
        else:
            object_type = 'Circle'

        cv2.putText(img_contour, object_type, (x + (w // 2) - len(object_type) * 4, y -10), cv2.FONT_HERSHEY_COMPLEX,
                    0.5, (0, 0, 0), 1)


def main():
    img = cv2.imread('imgs/red_onion_original/red_onion_108.jpg')
    print(img.shape)

    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    cv2.namedWindow('Trackbars')
    cv2.resizeWindow('Trackbars', 640, 240)
    cv2.createTrackbar('Hue Min', 'Trackbars', 99, 179, lambda x: 0)
    cv2.createTrackbar('Hue Max', 'Trackbars', 123, 179, lambda x: 0)
    cv2.createTrackbar('Sat Min', 'Trackbars', 80, 255, lambda x: 0)
    cv2.createTrackbar('Sat Max', 'Trackbars', 255, 255, lambda x: 0)
    cv2.createTrackbar('Val Min', 'Trackbars', 148, 255, lambda x: 0)
    cv2.createTrackbar('Val Max', 'Trackbars', 255, 255, lambda x: 0)

    while True:
        hue_min = cv2.getTrackbarPos('Hue Min', 'Trackbars')
        hue_max = cv2.getTrackbarPos('Hue Max', 'Trackbars')
        sat_min = cv2.getTrackbarPos('Sat Min', 'Trackbars')
        sat_max = cv2.getTrackbarPos('Sat Max', 'Trackbars')
        val_min = cv2.getTrackbarPos('Val Min', 'Trackbars')
        val_max = cv2.getTrackbarPos('Val Max', 'Trackbars')

        lower_limit = np.array([hue_min, sat_min, val_min])
        upper_limit = np.array([hue_max, sat_max, val_max])
        mask = cv2.inRange(img_hsv, lower_limit, upper_limit)

        masked_image = cv2.bitwise_and(img, img, mask=mask)
        image_stacked = stack_images(0.5, ([img_hsv], [mask], [masked_image]))
        cv2.imshow('Images', image_stacked)
        cv2.waitKey(1)

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img_blur = cv2.GaussianBlur(img_gray, (7, 7), 0.5)

    img_canny1 = cv2.Canny(img_gray, 30, 200)
    img_canny2 = cv2.Canny(img_gray, 200, 300)

    kernel = np.ones((5, 5), np.uint8)

    img_dilate = cv2.dilate(img_canny1, kernel, iterations=1)
    img_erode = cv2.erode(img_dilate, kernel, iterations=1)

    img_contour = img_gray.copy()
    get_contours(img_canny1, img_contour)
    stacked_imgs = stack_images(0.5, ([img_gray, img_blur, img_canny1, img_canny2],
                                      [img_dilate, img_erode, img, img_contour]))
    cv2.imshow('Stacked together', stacked_imgs)

    for i in range(71):
        img = cv2.imread(f'./imgs/red_onion_original/red_onion_{i + 72}.jpg')
        grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur_img = cv2.GaussianBlur(grey_img, (7, 7), 2)
        canny_img = cv2.Canny(blur_img, 13, 29)
        cv2.imwrite(f'./red_onion_contours/red_onion_contours{i + 1}.jpg', canny_img)


if __name__ == '__main__':
    main()

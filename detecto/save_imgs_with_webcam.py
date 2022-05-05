from datetime import datetime

import cv2
import os


def show_webcam(mirror=False, cam_id=0, save_file='image'):
    cam = cv2.VideoCapture(cam_id)
    img_count = 109
    last_sec = -1
    while True:
        ret_val, img = cam.read()
        if mirror:
            img = cv2.flip(img, 1)
        cv2.imshow('my webcam', img)
        if cv2.waitKey(1) == 27:
            break  # esc to quit

        t = datetime.now()
        if t.second % 2 == 0 and t.second != last_sec:
            last_sec = t.second
            imgname = f'./imgs/{save_file}_{img_count}.jpg'
            print('Saving', imgname)
            img_count += 1
            cv2.imwrite(imgname, img)

    cv2.destroyAllWindows()


def main():
    # show_webcam()

    folder = 'imgs/cucumber/training'
    for count, filename in enumerate(os.listdir(folder)):
        count += 1
        dst = f'red_onion_{str(count)}.jpg'
        src = f'{folder}/{filename}'
        dst = f'{folder}/{dst}'

        os.rename(src, dst)

if __name__ == '__main__':
    main()

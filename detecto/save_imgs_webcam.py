from datetime import datetime
import cv2


def show_webcam(mirror=False, cam_id=1, save_file='image_veg'):
    cam = cv2.VideoCapture(cam_id)
    img_count = 1
    last_sec = -1
    while True:
        ret_val, img = cam.read()
        if mirror:
            img = cv2.flip(img, 1)
        cv2.imshow('my webcam', img)
        if cv2.waitKey(1) == 27:
            break  # esc to quit

        t = datetime.now()
        if t.second % 5 == 0 and t.second != last_sec:
            last_sec = t.second
            img_name = f'./images/{save_file}_{img_count}.jpg'
            print('Saving', img_name)
            img_count += 1
            cv2.imwrite(img_name, img)

    cam.release()
    cv2.destroyAllWindows()


def main():
    show_webcam()


if __name__ == '__main__':
    main()

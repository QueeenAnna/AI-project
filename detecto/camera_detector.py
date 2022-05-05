import cv2

# The number inside the parentheses decides how many cameras will be used
cam = cv2.VideoCapture(1)

while True:
    # Two frames is needed to see the movement, ret means if something has succeeded or not
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()
    # The difference between the two frames
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Choose this for loop to get rectangles around the object ...
    # for c in contours:
    #     if cv2.contourArea(c) < 5000:
    #         continue
    #     x, y, w, h = cv2.boundingRect(c)
    #     cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 3)

    # ... or this to get the contours
    cv2.drawContours(frame1, contours, -1, (0, 255, 0), 4)

    cv2.imshow('Food Camera', frame1)

    if cv2.waitKey(10) & 0xFF == ord('d'):
        break

cam.release()
cv2.destroyWindow()


def main():
    pass


if __name__ == '__main__':
    main()

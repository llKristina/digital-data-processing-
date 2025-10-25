import cv2
import numpy as np

def task1():
    cap=cv2.VideoCapture(0)
    

    while True:
        ret, frame=cap.read()
        if not ret:
            break
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        cv2.imshow("webcam",hsv)
        if cv2.waitKey(1) & 0xFF==27:
            break
# task1()

def task2():
    imgl=cv2.imread(r"pic.jpg")
    img = cv2.resize(imgl, (400, 500)) 

    lower_red = np.array([0, 0, 120])
    upper_red = np.array([80, 80, 255])
    mask = cv2.inRange(img, lower_red, upper_red)

    cv2.imshow("mask", mask)
    cv2.imshow("Original", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# task2()

def task3():
    imgl = cv2.imread("pic.jpg")
    img = cv2.resize(imgl, (400, 500)) 
    lower_red = np.array([0, 0, 120])
    upper_red = np.array([80, 80, 255])
    mask = cv2.inRange(img, lower_red, upper_red)

    kernel = np.ones((3, 3), np.uint8)  
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    cv2.imshow("Original", img)
    cv2.imshow("Threshold", mask)
    cv2.imshow("Opening (erode->dilate)", opening)
    cv2.imshow("Closing (dilate->erode)", closing)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# task3()


def task45():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_red1 = np.array([0, 150, 150])
        upper_red1 = np.array([8, 255, 255])

        lower_red2 = np.array([172, 150, 150])
        upper_red2 = np.array([179, 255, 255])

        mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
        mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
        mask = cv2.bitwise_or(mask1, mask2)

        kernel = np.ones((5, 5), np.uint8)
        opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

        moments = cv2.moments(closing)
        area = moments['m00']

        if area > 100:
            cx = int(moments['m10'] / area)
            cy = int(moments['m01'] / area)

            ys, xs = np.where(closing > 0)
            if len(xs) > 0 and len(ys) > 0:
                x_min, x_max = np.min(xs), np.max(xs)
                y_min, y_max = np.min(ys), np.max(ys)
                cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 0, 0), 2)
                cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)

        cv2.imshow("tracking", frame)
        cv2.imshow("mask", closing)

        if cv2.waitKey(25) & 0xFF == 27:
            break
        
    cap.release()
    cv2.destroyAllWindows()
# task45()
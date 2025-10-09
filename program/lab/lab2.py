import cv2
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
task1()

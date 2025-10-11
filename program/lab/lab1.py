import cv2

def task2():
    img = cv2.imread(r"cat.jpg")
    cv2.namedWindow("CAT", cv2.WINDOW_NORMAL)
    cv2.imshow("CAT", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
# task2()

def task3():
    cap = cv2.VideoCapture("cat2.mp4")
    while cap.isOpened():
        ret, frame = cap.read()
        if not(ret):
            break
        frame = cv2.resize(frame, (550, 700))
        cv2.imshow("cat2.mp4",frame)
        if cv2.waitKey(1) & 0xFF ==27:
            break
# task3()

def task4():
    cap = cv2.VideoCapture("cat2.mp4")
    fourcc= cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter("output.mp4", fourcc, 25, (550, 700))
    while(True):
        ok, img = cap.read()
        if not ok:
            break
        img = cv2.resize(img, (550, 700))
        cv2.imshow('img',img)
        video_writer.write(img)
        if cv2.waitKey(1) & 0x77 == ord('q'):
            break
    cap.release()
    video_writer.release()
    cv2.destroyAllWindows()
# task4()

def task5():
    img = cv2.imread(r"cat.jpg")
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    img=cv2.resize(img,(350,350))
    hsv=cv2.resize(hsv,(350,350))
    cv2.imshow("original",img)
    cv2.imshow("HSV", hsv)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# task5()

def task6():
    cap = cv2.VideoCapture(0) 
 
    while True:
        ret, frame = cap.read()
        if not(ret):
            break

        h, w = frame.shape[:2]
        x, y = w // 2, h // 2
        cv2.rectangle(frame, (x-100, y-15), (x+100, y+15), (0, 0, 255), 2)
        cv2.rectangle(frame, (x-15, y-100), (x+15, y+100), (0, 0, 255), 2)

        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == 27:  
            break

    cap.release()
    cv2.destroyAllWindows()

# task6()

def task7():
    cap = cv2.VideoCapture(0)
    fps = cap.get(cv2.CAP_PROP_FPS)

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter("webcam_output.mp4", fourcc, fps, (width,height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)
        cv2.imshow("Webcam", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
# task7()


def task8():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        h, w = frame.shape[:2]
        x, y = w // 2, h // 2
        b, g, r = frame[y, x]

        if r >= g and r >= b:
            color = (0, 0, 255)  
            color_name = "Red"
        elif g >= r and g >= b:
            color = (0, 255, 0)  
            color_name = "Green"
        else:
            color = (255, 0, 0)  
            color_name = "Blue"

        cv2.rectangle(frame, (x - 100, y - 15), (x + 100, y + 15), color, -1)
        cv2.rectangle(frame, (x - 15, y - 100), (x + 15, y + 100), color, -1)

        cv2.putText(frame, f"Color: {color_name}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

# task8()

def task9():
    cap=cv2.VideoCapture(1)

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("Webcam", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

# task9()




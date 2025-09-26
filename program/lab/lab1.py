import cv2

#task 2
img = cv2.imread(r"cat.jpg")
cv2.namedWindow("CAT", cv2.WINDOW_NORMAL)
cv2.imshow("CAT", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#task 3
cap = cv2.VideoCapture("cat2.mp4")
while cap.isOpened():
    ret, frame = cap.read()
    if not(ret):
        break
    frame = cv2.resize(frame, (550, 700))
    cv2.imshow("cat2.mp4",frame)
    if cv2.waitKey(1) & 0xFF ==5:
        break

#task 4
cap = cv2.VideoCapture("cat2.mp4")
ok, img= cap.read()
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc= cv2.VideoWriter_fourcc(*'mp4v')
video_writer=cv2.VideoWriter("output.mp4",fourcc,25,(w,h))
while(True):
    ok, img = cap.read()
    img = cv2.resize(img, (550, 700))
    cv2.imshow('img',img)
    video_writer.write(img)
    if cv2.waitKey(1) & 0x77 == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
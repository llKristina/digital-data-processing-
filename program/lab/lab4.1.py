import cv2

def task1():
    img = cv2.imread(r'car.jpg')
    img = cv2.resize(img, (400, 600)) 
    cv2.imshow("Original", img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale", gray)
    blur = cv2.GaussianBlur(gray, (5, 5), 1.4)
    cv2.imshow("Gaussian Blur", blur)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
task1()
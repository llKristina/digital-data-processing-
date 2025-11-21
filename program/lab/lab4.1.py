import cv2
import numpy as np

def task1(path):
    img = cv2.imread(path)
    img = cv2.resize(img, (400, 600)) 
    cv2.imshow("Original", img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale", gray)
    blur = cv2.GaussianBlur(gray, (5, 5), 1.4)
    cv2.imshow("Gaussian Blur", blur)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
# task1("D:/pic/car.jpg")

def task2(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (400, 600)) 
    blur = cv2.GaussianBlur(img, (5, 5), 1.4)

    gx = cv2.Sobel(blur, cv2.CV_64F, 1, 0, ksize=3)
    gy = cv2.Sobel(blur, cv2.CV_64F, 0, 1, ksize=3)
    magnitude = np.sqrt(gx**2 + gy**2)

    angle = np.arctan2(gy, gx) * 180 / np.pi
    print("Матрица длин градиента:\n", magnitude)
    print("\nМатрица углов градиента:\n", angle)

    cv2.imshow("Gradient magnitude", magnitude / magnitude.max())
    cv2.waitKey(0)
    cv2.destroyAllWindows()

task2("D:/pic/car.jpg")


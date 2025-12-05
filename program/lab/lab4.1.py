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
    return magnitude, angle


def task3(mag, angle):
    H, W = mag.shape
    output = np.zeros((H, W), dtype=np.float32)

    # Приводим углы к 0, 45, 90, 135
    angle = angle % 180

    for i in range(1, H-1):
        for j in range(1, W-1):
            q = 255
            r = 255

            # 0 градусов
            if (0 <= angle[i,j] < 22.5) or (157.5 <= angle[i,j] <= 180):
                q = mag[i, j+1]
                r = mag[i, j-1]

            # 45 градусов
            elif (22.5 <= angle[i,j] < 67.5):
                q = mag[i+1, j-1]
                r = mag[i-1, j+1]

            # 90 градусов
            elif (67.5 <= angle[i,j] < 112.5):
                q = mag[i+1, j]
                r = mag[i-1, j]

            # 135 градусов
            elif (112.5 <= angle[i,j] < 157.5):
                q = mag[i-1, j-1]
                r = mag[i+1, j+1]

            if mag[i,j] >= q and mag[i,j] >= r:
                output[i,j] = mag[i,j]
            else:
                output[i,j] = 0

    return output

#двойная пороговая фильтрация
def double_threshold(img, low, high):
    strong = 255
    weak = 75

    result = np.zeros_like(img, dtype=np.uint8)

    strong_pixels = img >= high
    weak_pixels = (img >= low) & (img < high)

    result[strong_pixels] = strong
    result[weak_pixels] = weak

    return result

# Задание 4 — гистерезис
def hysteresis(img):
    H, W = img.shape
    strong = 255
    weak = 75

    for i in range(1, H - 1):
        for j in range(1, W - 1):
            if img[i, j] == weak:
                if np.any(img[i - 1:i + 2, j - 1:j + 2] == strong):
                    img[i, j] = strong
                else:
                    img[i, j] = 0

    return img

def task4(path, low=20, high=60):
    magnitude, angle = task2(path)
    nms = task3(magnitude, angle)

    nms_norm = (nms / np.max(nms) * 255).astype(np.uint8)

    dt = double_threshold(nms_norm, low, high)
    final_edges = hysteresis(dt.copy())

    cv2.imshow("NMS", nms_norm)
    cv2.imshow("Double Threshold", dt)
    cv2.imshow("Final edges (Hysteresis)", final_edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return final_edges

task4("D:/pic/car.jpg", low=25, high=60)



# Задание 5 — эксперименты 
def task5(path, sigmas, low_vals, high_vals):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (400, 600))

    for sigma in sigmas:
        print(f"Sigma = {sigma}")
        blur = cv2.GaussianBlur(img, (5, 5), sigma)

        gx = cv2.Sobel(blur, cv2.CV_64F, 1, 0, ksize=3)
        gy = cv2.Sobel(blur, cv2.CV_64F, 0, 1, ksize=3)
        magnitude = np.sqrt(gx**2 + gy**2)
        angle = np.arctan2(gy, gx)

        nms = task3(magnitude, angle)
        nms_norm = (nms / np.max(nms) * 255).astype(np.uint8)
        for low in low_vals:
            for high in high_vals:
                if high <= low:
                    continue

                print(f"Testing: low={low}, high={high}")

                dt = double_threshold(nms_norm, low, high)
                hyst = hysteresis(dt.copy())

                cv2.imshow(f"Sigma={sigma}, low={low}, high={high}", hyst)
                cv2.waitKey(400)

    cv2.destroyAllWindows()

# task5(
#     "D:/pic/car.jpg",
#     sigmas=[0.5, 1.0, 1.4, 2.0],
#     low_vals=[10, 20, 30],
#     high_vals=[40, 60, 80]
# )


import cv2
import numpy as np

# input: dau vao anh tao
# tinh ra threshold
# kich thuoc pixel - kich thuoc that ->>> kich thuoc tao
# output: kich thuoc to nho

# khoang cach tu bang tai - camera: 24.5 cm
# kich thuoc qua thuc te: 8 cm
# pixel w h 275 254 pixel
# tieu cu camera 778
# tao to la tao co ban kinh >= 3.25 nho la ban kinh < 3.25
THRESH_AREA_SIZE = 3.25*3.25*3.14

def phan_loai_to_nho(input_image, color):
    # image = cv2.resize(image, fx=0.3, fy=0.3, dsize=None)
    hsv = cv2.cvtColor(input_image, cv2.COLOR_BGR2HSV)
    if color == 1:  # detect mau do
        th1 = cv2.inRange(hsv, np.array([0, 70, 50]), np.array([20, 255, 255]))
        th2 = cv2.inRange(hsv, np.array([170, 70, 50]), np.array([180, 255, 255]))
        result = cv2.add(th1, th2)
    elif color == 0:  # detect mau xanh
        result = cv2.inRange(hsv, np.array([36,0,0]), np.array([66,200, 200]))

    kernel = np.ones((5, 5), np.uint8)
    opening = cv2.morphologyEx(result, cv2.MORPH_OPEN, kernel, iterations=3)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel, iterations=3)
    canny = cv2.Canny(closing.copy(), 100, 200)
    contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    areas = [cv2.contourArea(c) for c in contours]
    max_index = np.argmax(areas)
    cnt = contours[max_index]

    x, y, w, h = cv2.boundingRect(cnt)
    # cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    # print(w, h)

    (x, y), radius = cv2.minEnclosingCircle(cnt)
    center = (int(x), int(y))
    radius = int(radius)
    cv2.circle(input_image, center, radius, (0, 255, 0), 2)

    ban_kinh_real = 24.5 * (radius/778)
    area_size = 3.14*ban_kinh_real*ban_kinh_real
    if area_size >= THRESH_AREA_SIZE:
        x = "to"
        return input_image, x  # qua to
    else:
        x = "nho"
        return input_image, x  # qua nho
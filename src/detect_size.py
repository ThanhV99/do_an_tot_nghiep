import cv2
import numpy as np

# input: dau vao anh tao
# tinh ra threshold
# kich thuoc pixel - kich thuoc that ->>> kich thuoc tao
# output: kich thuoc to nho
KERNEL = np.ones((5, 5))

def phan_loai_to_nho(input_image):
    if input_image is None:
        return input_image

    blur = cv2.GaussianBlur(input_image, (5, 5), 0)
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)
    closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel=KERNEL)

    canny = cv2.Canny(closing, 200, 230)
    # circles
    circles = cv2.HoughCircles(canny, cv2.HOUGH_GRADIENT, 1, 20, param1=200, param2=20, minRadius=1, maxRadius=50)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for (x, y, r) in circles[0, :]:
            cv2.circle(input_image, (x, y), 1, (0, 0, 255), 3)
            cv2.circle(input_image, (x, y), r, (0, 255, 0), 3)

    return input_image
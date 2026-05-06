import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('../src/Photos/lady.jpg')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Asli", img)
# cv.imshow('Gray', img_gray)
median = np.median(img_gray)

# print(f'Tinggi, lebar: {img_gray.shape}')
# print(f'Total pixel: {img_gray.size}')
# print(f'Pixel data type: {img_gray.dtype}')
# print(f'Median: {median}')

# hist = cv.calcHist([img_gray], [0], None, [256], [0, 256])
# plt.plot(hist)
# plt.title("Gray Lady Histogram")
# plt.xlabel("Pixel Intensity")
# plt.ylabel('Frequency')
# plt.show()

blur = cv.GaussianBlur(img_gray, (3,3), 0)
edges = cv.Canny(blur, 150, 200)
# cv.imshow('blur', blur)
# cv.imshow('canny', edges)

kernel_dilate = cv.getStructuringElement(cv.MORPH_ELLIPSE, (15, 15))
dilated = cv.dilate(edges, kernel_dilate, iterations=1)
# cv.imshow('dilated', dilated)

kernel_close = cv.getStructuringElement(cv.MORPH_ELLIPSE, (7,7))
closed = cv.morphologyEx(dilated, cv.MORPH_CLOSE, kernel_close)
# cv.imshow('closed', closed)

kernel = np.ones((7,7), np.uint8)
eroded = cv.erode(closed, kernel, iterations=6)

cv.imshow('eroded', eroded)

kernel_dilate_2 = cv.getStructuringElement(cv.MORPH_ELLIPSE, (13, 13))
dilated_2 = cv.dilate(eroded, kernel_dilate_2, iterations=8)
cv.imshow('dilated 2', dilated_2)

# kernel_2 = np.ones((7,7), np.uint8)
# eroded_2 = cv.erode(dilated_2, kernel, iterations=4)
# cv.imshow('eroded 2', eroded_2)

contours,_ = cv.findContours(dilated_2, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    x, y, w, h = cv.boundingRect(cnt)
    area = cv.contourArea(cnt)

    if area > 100:
        cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

        label = 'Lady'
        font = cv.FONT_HERSHEY_SIMPLEX
        font_scale = 0.6
        color = (0, 255, 0)
        thicknes = 2

        cv.putText(img, label, (x, y - 10), font, font_scale, color, thicknes)

# for cnt in contours:
#     x, y, w, h = cv.boundingRect(cnt)
#     area = cv.contourArea(cnt)
#     aspect_ratio = w / h if h > 0 else 0

#     # Wajah manusia rasionya mendekati 0.75–1.3
#     # dan posisinya di bagian atas gambar
#     img_height = img.shape[0]
#     if area > 10000 and 0.6 < aspect_ratio < 1.4 and y < img_height * 0.5:
#         cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv.imshow('gambar', img)

cv.waitKey(0)
cv.destroyAllWindows()
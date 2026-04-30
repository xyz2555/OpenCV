import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('../src/Photos/cats 2.jpg')
img_gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

median = np.median(img_gray)

print(f'Tinggi, lebar: {img_gray.shape}')
print(f'Total pixel: {img_gray.size}')
print(f'Pixel data type: {img_gray.dtype}')
print(f'Median: {median}')

# hist = cv.calcHist([img_gray], [0], None, [256], [0, 256])
# plt.plot(hist)
# plt.title("Gray Cat Histogram")
# plt.xlabel("Pixel Intensity")
# plt.ylabel('Frequency')
# plt.show()

# sift = cv.SIFT_create()
# orb = cv.ORB_create()

# keypoints, descriptors = sift.detectAndCompute(img_gray, None)
# keypoints2, descriptors2 = orb.detectAndCompute(img_gray, None)
# image_with_keypoints = cv.drawKeypoints(img_gray, keypoints2, None, color=(0, 255, 0))

# output = cv.drawKeypoints(img_gray, keypoints, None)

# cv.imshow('sift keypoints', output)

# plt.imshow(image_with_keypoints)
# plt.show()

gray_blur = cv.GaussianBlur(img_gray, (3, 3), 0)
# edges = cv.Canny(gray_blur, int(max(0, (1.0 - 0.37) * median)), int(min(255, (1.0 + 0.37) * median)))
edges = cv.Canny(gray_blur, 0, 180)
# cv.imshow('blur', gray_blur)
# cv.imshow('canny', edges)

kernel_dilate = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
dilated = cv.dilate(edges, kernel_dilate, iterations=1)
# cv.imshow('dilated', dilated)

kernel_close = cv.getStructuringElement(cv.MORPH_ELLIPSE, (9, 9))
closed = cv.morphologyEx(dilated, cv.MORPH_CLOSE, kernel_close)
cv.imshow('closed', closed)

contours,_ = cv.findContours(closed, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
# cv.drawContours(img, contours, -1, (0, 255, 0), 2)
# cv.imshow('hasil draw', img)

# def classify(w, h, area):
#     if h == 0:
#         return 'Abaikan'

for cnt in contours:
    x, y, w, h = cv.boundingRect(cnt)
    area = cv.contourArea(cnt)

    if area > 50:
        cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv.imshow('gambar', img)

cv.waitKey(0)
cv.destroyAllWindows()
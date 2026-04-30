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
edges = cv.Canny(gray_blur, int(max(0, (1.0 - 0.37) * median)), int(min(255, (1.0 + 0.37) * median)))
cv.imshow('blur', gray_blur)
cv.imshow('canny', edges)

cv.waitKey(0)
cv.destroyAllWindows()
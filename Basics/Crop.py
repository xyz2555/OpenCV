import cv2 as cv

img = cv.imread("../src/Photos/cat.jpg")
cv.imshow("Cat", img)

cropped = img[50:200, 200:400]   # Memotong (crop) sebagian area gambar dari koordinat y=50:200 dan x=200:400
cv.imshow('Cropped', cropped)    # Menampilkan hasil potongan gambar

cv.waitKey(0)

# Ringkasan:
# Program ini membaca gambar dan menampilkan hasil potongan (crop) pada area tertentu dari gambar aslinya.

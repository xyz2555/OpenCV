import cv2 as cv

img = cv.imread("../src/Photos/cat.jpg")   
cv.imshow('Cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)   # Mengonversi gambar dari format warna BGR ke Grayscale (hitam-putih)
cv.imshow('Gray Image', gray)                # Menampilkan hasil gambar dalam mode grayscale

cv.waitKey(0)

# Ringkasan:
# Program ini membaca gambar berwarna dan mengubahnya menjadi citra grayscale menggunakan fungsi cvtColor.

import cv2 as cv

img = cv.imread("../src/Photos/cat.jpg")   
cv.imshow('Cat', img)

blur = cv.GaussianBlur(img, (9,9), cv.BORDER_DEFAULT)   # Menerapkan efek blur pada gambar menggunakan metode Gaussian Blur dengan ukuran kernel 9x9
cv.imshow('Blur', blur)   # Menampilkan hasil gambar yang sudah di-blur

cv.waitKey(0)

# Ringkasan:
# Program ini membaca gambar kucing, kemudian menerapkan efek Gaussian Blur untuk menghaluskan detail gambar.

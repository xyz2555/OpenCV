import cv2 as cv  # import library OpenCV
import numpy as np  # import numpy untuk operasi matriks

# Membaca gambar dari file dengan format BGR (Blue, Green, Red)
img = cv.imread('../src/Photos/park.jpg')
cv.imshow('park', img)  # menampilkan gambar asli

# Mengubah gambar dari BGR ke grayscale
# Edge detection biasanya bekerja pada citra grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# ----------------------------------------
# LAPLACIAN EDGE DETECTION
# ----------------------------------------

# Menghitung gradien ke-2 (second derivative) dari gambar
# CV_64F digunakan agar nilai gradien tidak terpotong saat negatif
lap = cv.Laplacian(gray, cv.CV_64F)

# Mengubah nilai gradien ke format uint8 (positif 0–255)
# np.absolute untuk mengubah nilai negatif menjadi positif
lap = np.uint8(np.absolute(lap))

cv.imshow('laplacian', lap)  # menampilkan hasil deteksi tepi laplacian

# ----------------------------------------
# SOBEL EDGE DETECTION (DERIVATIVE PERTAMA)
# ----------------------------------------

# Menghitung gradien pada arah X (mendeteksi tepi vertikal)
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)

# Menghitung gradien pada arah Y (mendeteksi tepi horizontal)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)

# Menggabungkan kedua hasil sobel dengan operasi OR
# sehingga kedua tepi (horizontal dan vertikal) ditampilkan
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('Sobel x', sobelx)
cv.imshow('Sobel y', sobely)
cv.imshow('combined sobel', combined_sobel)

# ----------------------------------------
# CANNY EDGE DETECTION
# ----------------------------------------

# Canny menggunakan kombinasi Gaussian blur + gradient + non-max suppression
# Threshold bawah = 150, threshold atas = 175
canny = cv.Canny(gray, 150, 175)

cv.imshow('canny', canny)  # deteksi tepi dengan metode canny

cv.waitKey(0)  # menunggu input keyboard

# --------------------------------------------------------------------
# RANGKUMAN:
# Kode ini melakukan deteksi tepi menggunakan beberapa metode:
# 1. Laplacian: menghitung second derivative, mendeteksi perubahan intensitas cepat
# 2. Sobel X dan Y: menghitung first derivative untuk tepi vertikal dan horizontal
# 3. Combined Sobel: menggabungkan tepi dari Sobel X dan Sobel Y
# 4. Canny: metode edge detection lanjutan yang lebih akurat dan bersih
#
# Tujuan utama kode ini: membandingkan berbagai teknik edge detection
# dan melihat hasil perbedaan masing-masing pada satu gambar yang sama.
# --------------------------------------------------------------------

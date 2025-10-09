import cv2 as cv
import numpy as np   # Digunakan untuk membuat matriks transformasi translasi

img = cv.imread("../src/Photos/cat.jpg")
cv.imshow("Cat", img)

def translate(img, x, y):   # Fungsi untuk menggeser (translasi) posisi gambar
    transMat = np.float32([[1, 0, x], [0, 1, y]])   # Matriks translasi untuk pergeseran sejauh x dan y piksel
    dimensions = (img.shape[1], img.shape[0])       # Menentukan ukuran gambar hasil translasi
    return cv.warpAffine(img, transMat, dimensions)  # Menerapkan transformasi translasi ke gambar

# Keterangan arah translasi:
# -x = geser ke kiri
# -y = geser ke atas
#  x = geser ke kanan
#  y = geser ke bawah

translated = translate(img, 100, -100)   # Menggeser gambar 100 piksel ke kanan dan 100 piksel ke atas
cv.imshow("Translated", translated)

cv.waitKey(0)

# Ringkasan:
# Program ini menggeser posisi gambar menggunakan transformasi translasi (warpAffine) dengan matriks translasi 2x3.

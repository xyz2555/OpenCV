import cv2 as cv           # Mengimpor library OpenCV dan memberi alias 'cv' untuk mempermudah penulisan fungsi-fungsinya
import numpy as np         # Mengimpor NumPy untuk operasi array/matrix, umumnya dibutuhkan untuk manipulasi gambar

img = cv.imread("../src/Photos/cats.jpg")   # Membaca file gambar dari path tertentu dan menyimpannya dalam variabel 'img' sebagai array (matrix) BGR
cv.imshow("Cats", img)                      # Menampilkan gambar asli dalam sebuah window berjudul "Cats"

blank = np.zeros(img.shape, dtype='uint8')  # Membuat gambar kosong (berwarna hitam) dengan ukuran yang sama seperti 'img'
cv.imshow("blank", blank)                   # Menampilkan gambar kosong untuk keperluan menggambar hasil contour nanti

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # Mengubah gambar dari format BGR ke grayscale (abu-abu) untuk mempermudah deteksi kontur
cv.imshow("gray", gray)                     # Menampilkan gambar dalam mode grayscale

# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)   # (Opsional) Memburamkan gambar untuk mengurangi noise agar deteksi tepi lebih stabil
# cv.imshow("blur", blur)

canny = cv.Canny(img, 125, 175)             # Melakukan edge detection (deteksi tepi) dengan algoritma Canny menggunakan threshold 125 dan 175
cv.imshow("canny", canny)                   # Menampilkan hasil gambar tepi

# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)  # (Opsional) Membuat gambar biner (hitam/putih) berdasarkan threshold tertentu
# cv.imshow("thresh", thresh)

contours, hierarchies = cv.findContours(    # Mencari kontur dari hasil deteksi tepi (Canny)
    canny,                                  # Input gambar yang berisi tepi
    cv.RETR_LIST,                           # Mode retrieval: mengambil SEMUA kontur tanpa membuat hubungan antar kontur (flat list)
    cv.CHAIN_APPROX_SIMPLE                  # Menyederhanakan titik-titik kontur agar lebih hemat memori
)
print(f'{len(contours)} contours found')    # Menampilkan jumlah kontur yang berhasil ditemukan pada gambar

cv.drawContours(blank, contours, -1, (0,0,255), 1) # Menggambar SEMUA kontur (-1) pada gambar kosong 'blank' dengan warna merah dan ketebalan garis 1
cv.imshow('draw contours', blank)           # Menampilkan hasil gambar yang berisi kontur

cv.waitKey(0)                               # Menunggu input keyboard sebelum menutup semua window OpenCV


# =======================================================================
# KEGUNAAN KESELURUHAN CODE INI
# =======================================================================
# Code ini digunakan untuk:
# 1. Membaca sebuah gambar.
# 2. Mengubahnya menjadi grayscale.
# 3. Melakukan pendeteksian tepi menggunakan algoritma Canny.
# 4. Mencari kontur yang terdapat pada gambar.
# 5. Menggambar seluruh kontur pada canvas kosong (blank).
# 6. Menampilkan gambar-gambar tersebut untuk visualisasi.
# Dengan kata lain, ini adalah pipeline dasar untuk "Contour Detection" di OpenCV.
# =======================================================================

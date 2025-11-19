import cv2 as cv                                   # Mengimpor library OpenCV untuk operasi pengolahan gambar
import numpy as np                                 # Mengimpor NumPy untuk membuat array (image = array)

blank = np.zeros((400,400), dtype='uint8')         # Membuat canvas kosong ukuran 400x400 dengan tipe uint8 (gambar hitam)

rectangle = cv.rectangle(                          # Menggambar persegi panjang (rectangle) pada canvas kosong
    blank.copy(),                                  # Menggunakan salinan canvas agar tidak mengubah "blank" asli
    (30,30),                                       # Titik kiri atas
    (370,370),                                     # Titik kanan bawah
    255,                                           # Warna putih (255 = putih pada grayscale)
    -1                                             # -1 artinya fill (diisi penuh)
)
circle = cv.circle(                                # Menggambar lingkaran pada canvas kosong
    blank.copy(),                                  # Menggunakan salinan canvas
    (200,200),                                     # Titik pusat lingkaran
    200,                                           # Radius 200
    255,                                           # Warna putih
    -1                                             # Diisi penuh
)

cv.imshow('rectangle', rectangle)                  # Menampilkan gambar persegi panjang
cv.imshow('circle', circle)                        # Menampilkan gambar lingkaran

bitwise_and = cv.bitwise_and(rectangle, circle)    # Operasi AND antara rectangle & circle
                                                    # Hanya area yang OVERLAP / tumpang tindih yang akan terlihat putih
cv.imshow('bitwise and', bitwise_and)               # Menampilkan hasil AND

bitwise_or = cv.bitwise_or(rectangle, circle)       # Operasi OR antara rectangle & circle
                                                    # Semua area yang merupakan rectangle ATAU circle akan terlihat putih
cv.imshow('bitwise or', bitwise_or)                 # Menampilkan hasil OR

bitwise_xor = cv.bitwise_xor(rectangle, circle)     # Operasi XOR (exclusive OR)
                                                    # Area yang berbeda (ada di salah satu tetapi bukan keduanya)
                                                    # Area overlap akan menjadi hitam
cv.imshow('bitwise xor', bitwise_xor)               # Menampilkan hasil XOR

bitwise_not = cv.bitwise_not(rectangle)             # Operasi NOT (kebalikan warna)
                                                    # Putih → hitam, hitam → putih
cv.imshow('bitwise not', bitwise_not)               # Menampilkan hasil NOT

cv.waitKey(0)                                       # Menunggu input sebelum menutup semua jendela


# =======================================================================
# KEGUNAAN KESELURUHAN CODE INI
# =======================================================================
# Code ini digunakan untuk mempelajari **operasi bitwise** pada gambar
# menggunakan OpenCV. Operasi ini sangat penting untuk:
#   - Masking
#   - Segmentasi objek
#   - Menggabungkan gambar
#   - Menentukan area tumpang tindih
#
# Yang dipelajari:
# 1. bitwise_and → Menampilkan area tumpang tindih antara dua bentuk.
# 2. bitwise_or  → Menggabungkan semua area dari kedua bentuk.
# 3. bitwise_xor → Menampilkan area yang berbeda (tidak overlap).
# 4. bitwise_not → Inveri warna, putih menjadi hitam dan sebaliknya.
#
# Operasi ini adalah dasar dalam banyak aplikasi seperti:
#   - Menyembunyikan objek tertentu
#   - Membuat mask untuk filtering warna
#   - Mengisolasi objek pada background hitam
# =======================================================================

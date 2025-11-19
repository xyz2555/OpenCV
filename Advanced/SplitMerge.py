import cv2 as cv                               # Mengimpor library OpenCV untuk manipulasi gambar
import numpy as np                             # Mengimpor NumPy untuk membuat dan memanipulasi array (gambar adalah array)

img = cv.imread("../src/Photos/park.jpg")      # Membaca gambar dari file dalam format BGR
cv.imshow("park", img)                         # Menampilkan gambar asli

blank = np.zeros(img.shape[:2], dtype='uint8') # Membuat gambar kosong (hitam) hanya dengan 1 channel (grayscale)
                                               # img.shape[:2] = (height, width)

b, g, r = cv.split(img)                        # Memisahkan gambar BGR menjadi tiga channel terpisah:
                                               # b = channel biru
                                               # g = channel hijau
                                               # r = channel merah

blue = cv.merge([b, blank, blank])             # Menggabungkan channel biru bersamaan dengan 2 channel kosong
                                               # Hasilnya: hanya channel biru yang terlihat (hijau & merah = 0)

green = cv.merge([blank, g, blank])            # Hanya channel hijau yang ditampilkan

red = cv.merge([blank, blank, r])              # Hanya channel merah yang ditampilkan

cv.imshow('Blue', blue)                        # Menampilkan gambar yang hanya berisi channel biru
cv.imshow('Green', green)                      # Menampilkan channel hijau
cv.imshow('Red', red)                          # Menampilkan channel merah

print(img.shape)                               # Menampilkan ukuran gambar asli, misalnya: (height, width, 3)
print(b.shape)                                 # Menampilkan ukuran channel biru   -> (height, width)
print(g.shape)                                 # Menampilkan ukuran channel hijau  -> (height, width)
print(r.shape)                                 # Menampilkan ukuran channel merah  -> (height, width)

merged = cv.merge([b, g, r])                   # Menggabungkan kembali ketiga channel BGR menjadi satu gambar lengkap
cv.imshow('merged', merged)                    # Menampilkan gambar hasil merge (harus sama seperti gambar asli)

cv.waitKey(0)                                  # Menunggu tombol keyboard sebelum menutup window OpenCV


# =======================================================================
# KEGUNAAN KESELURUHAN CODE INI
# =======================================================================
# Code ini digunakan untuk mempelajari bagaimana gambar BGR dibangun dari tiga
# channel warna terpisah:
#
# 1. Memisahkan gambar menjadi channel Biru, Hijau, Merah.
# 2. Menampilkan masing-masing channel secara visual.
# 3. Membuat visualisasi "hanya channel tertentu saja" dengan menggabungkan
#    satu channel dengan dua channel kosong.
# 4. Meneliti shape/dimensi masing-masing channel.
# 5. Menggabungkan kembali channel B, G, R menjadi satu gambar utuh.
#
# Ini adalah dasar penting untuk memahami manipulasi warna di OpenCV,
# terutama untuk filtering warna, masking, threshold warna, dan color segmentation.
# =======================================================================

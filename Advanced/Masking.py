import cv2 as cv                                       # Mengimpor library OpenCV untuk operasi pengolahan gambar
import numpy as np                                     # Mengimpor NumPy untuk membuat dan memanipulasi array (gambar)

img = cv.imread('../src/Photos/cats.jpg')              # Membaca gambar dari file dalam format BGR
cv.imshow('cats', img)                                 # Menampilkan gambar asli

blank = np.zeros(img.shape[:2], dtype='uint8')         # Membuat gambar kosong (hitam) dengan ukuran sama seperti gambar asli
                                                       # Hanya 1 channel (grayscale)
cv.imshow('blank', blank)                              # Menampilkan gambar blank (hitam)

mask = cv.circle(                                      # Membuat mask berbentuk lingkaran
    blank,                                             # Menggunakan canvas kosong
    (img.shape[1]//2, img.shape[0]//2),                # Titik pusat lingkaran = tengah gambar
    100,                                               # Radius lingkaran
    255,                                               # Warna putih (255) → area yang akan terlihat
    -1                                                 # -1 artinya lingkaran diisi penuh (filled)
)
cv.imshow('mask', mask)                                # Menampilkan mask lingkaran

rectangle = cv.rectangle(                              # Membuat mask berbentuk persegi panjang
    blank.copy(),                                      # Salinan blank agar tidak menimpa mask sebelumnya
    (30,30),                                           # Koordinat kiri atas
    (370,370),                                         # Koordinat kanan bawah
    255,                                               # Warna putih
    -1                                                 # Diisi penuh
)

circle = cv.circle(                                    # Membuat lingkaran kedua, sedikit bergeser ke kanan
    blank.copy(),                                      # Menggunakan salinan canvas lagi
    (img.shape[1]//2 + 45, img.shape[0]//2),           # Pusat lingkaran digeser 45 pixel ke kanan
    100,                                               # Radius
    255,                                               # Warna putih
    -1                                                 # Diisi penuh
)

weird_shape = cv.bitwise_and(circle, rectangle)        # Membuat shape dari area yang overlap antara persegi panjang & lingkaran
                                                       # Hanya area yang tumpang tindih yang berwarna putih
                                                       # Hasil inilah yang dipakai sebagai mask final

masked = cv.bitwise_and(img, img, mask=weird_shape)    # Menerapkan mask pada gambar asli
                                                       # 'mask=weird_shape' → hanya area putih pada weird_shape yang terlihat
cv.imshow('masked', masked)                            # Menampilkan gambar asli yang sudah dipotong oleh mask

cv.waitKey(0)                                          # Menunggu input sebelum menutup window


# =======================================================================
# KEGUNAAN KESELURUHAN CODE INI
# =======================================================================
# Code ini digunakan untuk mempelajari cara membuat mask kompleks dari
# beberapa bentuk (shape) dan menerapkannya ke gambar.
#
# Yang dilakukan:
# 1. Membuat canvas kosong (hitam).
# 2. Membuat beberapa bentuk, seperti rectangle dan circle.
# 3. Menggabungkan bentuk-bentuk tersebut menggunakan operasi bitwise
#    (bitwise_and) untuk membentuk mask dengan bentuk "aneh" (custom shape).
# 4. Menerapkan mask tersebut ke gambar asli sehingga hanya area tertentu
#    yang terlihat.
#
# Masking digunakan dalam berbagai aplikasi:
#   - Mengambil ROI (Region of Interest)
#   - Segmentasi objek
#   - Menyorot area tertentu pada gambar
#   - Membuat efek highlight
#   - Menghilangkan bagian gambar yang tidak diinginkan
# =======================================================================

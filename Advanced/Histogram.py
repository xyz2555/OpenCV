import cv2 as cv                                       # Library OpenCV untuk pengolahan gambar
import numpy as np                                     # NumPy untuk array
import matplotlib.pyplot as plt                        # Matplotlib untuk plotting grafik

img = cv.imread("../src/Photos/cats.jpg")              # Membaca gambar dari file (format BGR)
cv.imshow('cats', img)                                 # Menampilkan gambar asli

blank = np.zeros(img.shape[:2], dtype='uint8')         # Membuat canvas kosong hitam 1 channel
                                                       # Ukurannya sama dengan foto asli

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)           # Opsional: konversi gambar ke grayscale
# cv.imshow('gray', gray)

circle = cv.circle(                                    # Membuat mask berbentuk lingkaran
    blank,                                             # Menggunakan canvas blank
    (img.shape[1]//2, img.shape[0]//2),                # Titik pusat: tengah gambar
    100,                                               # Radius lingkaran
    255,                                               # Warna putih (area mask aktif)
    -2                                                 # Ketebalan -2 → fill penuh (mirip -1, variasi edge)
)
# NOTE: circle sekarang menjadi gambar 1 channel berisi lingkaran putih

mask = cv.bitwise_and(img, img, mask=circle)           # Menerapkan mask ke gambar asli
                                                       # Hanya area lingkaran yang terlihat
cv.imshow('mask', mask)                                # Menampilkan hasil masked area

# ------------------------------------------------------------------
# Contoh histogram grayscale (dikomentari)
# Menghitung histogram grayscale dari area yang dimask
# ------------------------------------------------------------------
# gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])
#
# plt.figure()
# plt.title('grayscale histogram')
# plt.xlabel('bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# ------------------------------------------------------------------
# Plot histogram dari masing-masing channel warna
# ------------------------------------------------------------------
plt.figure()                                           # Membuat figure baru untuk plot
plt.title('colors histogram')                          # Judul grafik
plt.xlabel('bins')                                     # Label sumbu X
plt.ylabel('# of pixels')                              # Label sumbu Y

colors = ('b', 'g', 'r')                               # Nama kanal warna

for i, col in enumerate(colors):                       # Loop 3 channel: B, G, R
    hist = cv.calcHist(                                # Menghitung histogram untuk channel ke-i
        [img],                                         # Sumber gambar
        [i],                                           # Channel yang dihitung (0=B,1=G,2=R)
        None,                                          # Tidak menggunakan mask (hitung seluruh gambar)
        [256],                                         # Banyak bin (0-255)
        [0,256]                                        # Rentang pixel
    )
    plt.plot(hist, color=col)                          # Plot histogram dengan warna sesuai channel
    plt.xlim([0,256])                                  # Batas sumbu X dari 0 ke 255

plt.show()                                             # Tampilkan plot histogram

cv.waitKey(0)                                          # Menunggu input sebelum tutup window


# =======================================================================
# KEGUNAAN KESELURUHAN CODE INI
# =======================================================================
# Code ini digunakan untuk mempelajari bagaimana:
#
# (1) Membuat mask berbentuk lingkaran dan menerapkannya pada gambar.
#     Mask digunakan untuk membatasi area yang ingin dianalisis atau ditampilkan.
#
# (2) Menghitung dan menampilkan histogram citra:
#     - Histogram adalah grafik yang menunjukkan seberapa banyak pixel
#       berada pada intensitas tertentu.
#
# (3) Mem-plot histogram untuk masing-masing channel warna (B, G, R)
#     secara terpisah.
#
# Tujuan histogram dalam visi komputer adalah:
#   - Menganalisis distribusi intensitas warna
#   - Menilai kontras gambar
#   - Deteksi objek
#   - Image segmentation
#   - Thresholding
#
# Fungsi utamanya dalam kode ini adalah untuk memahami bagaimana
# histogram warna bekerja dan bagaimana mem-visualisasikannya.
# =======================================================================

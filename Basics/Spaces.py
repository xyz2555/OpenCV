import cv2 as cv                         # Mengimpor library OpenCV untuk pengolahan gambar, memberi alias 'cv' agar lebih ringkas.
import matplotlib.pyplot as plt          # Mengimpor Matplotlib untuk menampilkan gambar dalam format RGB (umumnya untuk keperluan plotting)

img = cv.imread("../src/Photos/park.jpg")   # Membaca file gambar dan menyimpannya sebagai array BGR (format default OpenCV)
cv.imshow("Park", img)                      # Menampilkan gambar asli dalam jendela berjudul "Park"

# plt.imshow(img)                          # (Tidak digunakan) Menampilkan gambar dengan Matplotlib, namun warnanya akan salah
# plt.show()                               # karena OpenCV membaca gambar dalam BGR, bukan RGB.

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # Mengubah gambar dari format BGR ke grayscale (abu-abu)
cv.imshow("gray", gray)                     # Menampilkan gambar grayscale

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)    # Mengubah gambar dari BGR ke ruang warna HSV (Hue, Saturation, Value)
cv.imshow("hsv", hsv)                       # Menampilkan gambar dalam format HSV (akan terlihat aneh karena tidak sesuai tampilan normal)

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)    # Mengubah gambar dari BGR ke ruang warna LAB (lebih mendekati persepsi warna manusia)
cv.imshow("lab", lab)                       # Menampilkan representasi LAB (visualnya tampak tidak natural)

hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)  # Mengembalikan gambar dari HSV kembali ke BGR
cv.imshow("hsv 2 bgr", hsv_bgr)               # Menampilkan hasil konversi untuk melihat apakah gambar kembali seperti asli

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)      # Mengubah gambar dari BGR (OpenCV) ke RGB (format default Matplotlib)
cv.imshow("rgb", rgb)                         # Menampilkan gambar RGB (warnanya benar, namun tampil di UI OpenCV)

plt.imshow(rgb)                               # Menampilkan gambar menggunakan Matplotlib (warna akan benar karena sudah diubah ke RGB)
plt.show()                                    # Memunculkan plot

cv.waitKey(0)                                 # Menunggu tombol keyboard sebelum menutup semua window


# =======================================================================
# KEGUNAAN KESELURUHAN CODE INI
# =======================================================================
# Code ini digunakan untuk mempelajari berbagai konversi ruang warna (color space)
# dalam OpenCV dan cara menampilkannya:
#
# 1. Membaca gambar dalam format BGR (default OpenCV)
# 2. Mengubah gambar menjadi:
#       - Grayscale (B/W)
#       - HSV (Hue-Saturation-Value)
#       - LAB (Lightness-A/B channels)
#       - RGB (untuk Matplotlib)
# 3. Menampilkan hasil dari tiap konversi menggunakan OpenCV dan Matplotlib
#
# Tujuan utamanya adalah memahami bagaimana sebuah gambar dapat direpresentasikan
# dalam berbagai ruang warna dan kapan masing-masing warna digunakan.
# =======================================================================

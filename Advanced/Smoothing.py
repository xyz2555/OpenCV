import cv2 as cv                                   # Mengimpor library OpenCV untuk pengolahan gambar

img = cv.imread('../src/Photos/cats.jpg')          # Membaca gambar dari file dalam format BGR
cv.imshow('cats', img)                             # Menampilkan gambar asli

average = cv.blur(img, (3,3))                      # Melakukan "Average Blur" atau "Box Blur"
                                                   # Filter ini menghitung rata-rata pixel pada kernel 3x3
                                                   # Efek: gambar menjadi lebih halus, tetapi detail ikut hilang
cv.imshow('average', average)                      # Menampilkan hasil blur rata-rata

gauss = cv.GaussianBlur(img, (3,3), 0)             # Melakukan Gaussian Blur menggunakan kernel 3x3
                                                   # Gaussian menggunakan distribusi normal (lebih lembut dari average blur)
                                                   # Efek: mengurangi noise sambil mempertahankan tepi lebih baik
cv.imshow('gauss', gauss)                          # Menampilkan hasil Gaussian blur

median = cv.medianBlur(img, 3)                     # Melakukan Median Blur dengan kernel radius 3
                                                   # Filter ini mengganti setiap pixel dengan nilai median dari tetangga
                                                   # Sangat efektif untuk menghapus noise "salt-and-pepper"
cv.imshow('median', median)                        # Menampilkan hasil median blur

bilateral = cv.bilateralFilter(img, 20, 35, 25)    # Bilateral Filter: smoothing yang mempertahankan tepi (edge-preserving)
                                                   # Parameter:
                                                   #   20 = diameter area sampling
                                                   #   35 = sigmaColor -> seberapa jauh warna boleh berubah
                                                   #   25 = sigmaSpace -> seberapa jauh spasial boleh dihitung
                                                   # Efek: noise berkurang tanpa merusak tepi gambar
cv.imshow('bilateral', bilateral)                  # Menampilkan hasil bilateral filter

cv.waitKey(0)                                      # Menunggu input dari keyboard sebelum menutup semua window


# =======================================================================
# KEGUNAAN KESELURUHAN CODE INI
# =======================================================================
# Code ini digunakan untuk mempelajari berbagai teknik smoothing (blur) pada
# pengolahan gambar menggunakan OpenCV:
#
# 1. Average Blur     → Menghaluskan gambar dengan rata-rata sederhana (paling kasar).
# 2. Gaussian Blur    → Mengurangi noise dengan efek lebih natural dan lembut.
# 3. Median Blur      → Sangat efektif untuk menghilangkan noise salt-and-pepper.
# 4. Bilateral Filter → Menghaluskan gambar namun tetap menjaga tepi (edge-preserving).
#
# Tujuan utamanya adalah memahami perbedaan cara kerja berbagai jenis blur dan
# kapan masing-masing teknik sebaiknya digunakan.
# =======================================================================

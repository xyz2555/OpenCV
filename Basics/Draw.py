import cv2 as cv   
import numpy as np   # Import numpy untuk membuat array numerik (digunakan sebagai canvas gambar)

blank = np.zeros((500,500,3), dtype='uint8')   # Membuat gambar kosong (canvas) berwarna hitam ukuran 500x500 dengan 3 channel (RGB)
cv.imshow('Blank', blank)   

# blank[:] = 255,0,0   # Memberi warna biru penuh ke seluruh canvas
# cv.imshow('Blue', blank)

# blank[200:300, 300:400] = 255,0,0   # Memberi warna biru hanya pada area tertentu (kotak kecil)p
# cv.imshow('Blue Block', blank)

# cv.rectangle(blank, (0,0), (250,500), (0,255,0), thickness=-1)   # Membuat persegi panjang hijau (full filled) dari koordinat (0,0) ke (250,500)
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)   # Membuat persegi panjang hijau dari (0,0) ke tengah canvas
cv.imshow("Rectangle", blank)

cv.circle(blank, (250,250), 40, (255,0,0), thickness=3)   # Membuat lingkaran biru dengan radius 40, titik tengah di (250,250)
cv.imshow("Circle", blank)

cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)   # Membuat garis putih dari (0,0) ke titik tengah canvas
cv.imshow("Line", blank)

cv.putText(blank, "LOL", (225, 255), cv.FONT_HERSHEY_SCRIPT_COMPLEX, 1.0, (0,255,0), 2)   # Menambahkan teks "LOL" berwarna hijau di posisi (225,255)
cv.imshow("Text", blank)

cv.waitKey(0)   # Menunggu input tombol agar jendela tidak langsung tertutup

# Ringkasan:
# Program ini membuat canvas kosong lalu menggambar bentuk-bentuk sederhana
# (persegi panjang, lingkaran, garis, dan teks) menggunakan OpenCV.

import cv2 as cv  # import library OpenCV

# Membaca gambar dari file dengan format BGR (Blue, Green, Red)
img = cv.imread('../src/Photos/cats.jpg')
cv.imshow('cats', img)  # menampilkan gambar asli

# Mengubah gambar dari format BGR ke grayscale (1 channel intensitas)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)  # menampilkan gambar grayscale

# Melakukan thresholding sederhana:
# Pixel >= 150 menjadi 255 (putih), lainnya menjadi 0 (hitam)
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('simple thresholded', thresh)  # menampilkan hasil thresholding

# Melakukan thresholding inverse:
# Pixel >= 150 menjadi 0 (hitam), lainnya menjadi 255 (putih)
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('simple thresholded inverse', thresh_inv)  # menampilkan hasil thresholding inverse

# Melakukan adaptive thresholding:
# Ambang dihitung berdasarkan lingkungan sekitar pixel (lokal)
# menggunakan metode mean, ukuran blok 11, offset (C) = 3
adaptive_thresh = cv.adaptiveThreshold(
    gray, 255, 
    cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,
    11, 3
)
cv.imshow('adaptive thresholding', adaptive_thresh)  # menampilkan hasil adaptive threshold

cv.waitKey(0)  # menahan tampilan hingga ada input tombol

#Kode ini membaca gambar, mengubahnya ke grayscale, kemudian melakukan tiga jenis thresholding:
# Simple binary threshold
# Inverse binary threshold
# Adaptive (lokal) threshold
# Tujuannya untuk membandingkan bagaimana metode thresholding memisahkan objek dari background pada gambar.
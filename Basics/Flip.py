import cv2 as cv

img = cv.imread("../src/Photos/park.jpg")
cv.imshow("Park", img)

flip = cv.flip(img, 1)   # Membalik (flip) gambar.
# Parameter kedua menentukan arah pembalikan:
#   0  → flip vertikal (atas-bawah)
#   1  → flip horizontal (kiri-kanan)
#  -1  → flip kedua arah (atas-bawah dan kiri-kanan sekaligus)
cv.imshow("Flipped", flip)   # Menampilkan hasil gambar yang sudah dibalik

cv.waitKey(0)

# Ringkasan:
# Program ini membaca gambar dan menampilkan versi yang telah dibalik secara horizontal menggunakan fungsi cv.flip().

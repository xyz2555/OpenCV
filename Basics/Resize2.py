import cv2 as cv

img = cv.imread("../src/Photos/cat.jpg")
cv.imshow("Cat", img)

resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)   # Mengubah ukuran gambar menjadi 500x500 piksel
# Parameter 'interpolation' menentukan metode interpolasi yang digunakan saat mengubah ukuran:
#   - cv.INTER_NEAREST : Interpolasi paling sederhana (tetangga terdekat), cepat tapi kualitas rendah.
#   - cv.INTER_LINEAR  : Default, hasil cukup baik untuk memperkecil gambar.
#   - cv.INTER_AREA    : Cocok untuk memperkecil gambar, menghasilkan hasil halus.
#   - cv.INTER_CUBIC   : Cocok untuk memperbesar gambar, hasil lebih halus tapi lebih lambat.
#   - cv.INTER_LANCZOS4: Kualitas tinggi untuk memperbesar, namun paling berat secara komputasi.
cv.imshow("Resized", resized)

cv.waitKey(0)

# Ringkasan:
# Program ini membaca gambar lalu mengubah ukurannya menjadi 500x500 piksel
# menggunakan metode interpolasi cv.INTER_CUBIC untuk hasil lebih halus saat diperbesar.

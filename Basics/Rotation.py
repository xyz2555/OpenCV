import cv2 as cv

img = cv.imread("../src/Photos/park.jpg")
cv.imshow("Park", img)

def rotate(img, angle, rotPoint=None):   # Fungsi untuk memutar (rotate) gambar sebesar sudut tertentu
    (height, width) = img.shape[:2]      # Mendapatkan ukuran tinggi dan lebar gambar

    if rotPoint is None:                 # Jika titik rotasi tidak ditentukan, gunakan titik tengah gambar
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1)   # Membuat matriks rotasi dengan titik dan sudut tertentu
    dimensions = (width, height)                          # Menentukan ukuran output gambar hasil rotasi

    return cv.warpAffine(img, rotMat, dimensions)          # Menerapkan transformasi rotasi ke gambar menggunakan warpAffine

rotated = rotate(img, -90)   # Memutar gambar sebesar -90 derajat (arah berlawanan jarum jam)
cv.imshow("Rotated", rotated)

rotated2 = rotate(rotated, -45)   # Memutar ulang hasil sebelumnya sebesar -45 derajat
cv.imshow("Rotated Again", rotated2)

cv.waitKey(0)

# Ringkasan:
# Program ini memutar gambar menggunakan fungsi rotate() dengan memanfaatkan matriks transformasi rotasi.
# Gambar pertama diputar -90°, lalu hasilnya kembali diputar -45°.

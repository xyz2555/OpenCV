import cv2 as cv

img = cv.imread("../src/Photos/cat.jpg")   
cv.imshow('Cat', img)

canny = cv.Canny(img, 125, 175)   # Mendeteksi tepi (edges) pada gambar menggunakan algoritma Canny dengan threshold 125 dan 175
cv.imshow('Canny Edges', canny)

dilated = cv.dilate(canny, (7,7), iterations=3)   # Mempertebal hasil deteksi tepi menggunakan operasi dilasi dengan kernel 7x7 sebanyak 3 kali
cv.imshow("Dilated", dilated)

eroded = cv.erode(dilated, (7,7), iterations=3)   # Menipiskan kembali hasil dilasi menggunakan operasi erosi dengan kernel 7x7 sebanyak 3 kali
cv.imshow("Eroded", eroded)

cv.waitKey(0)

# Ringkasan:
# Program ini melakukan deteksi tepi pada gambar dengan Canny, lalu mempertebal dan menipiskan hasil tepi menggunakan operasi morfologi (dilate dan erode).

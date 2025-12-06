import cv2 as cv  # import library OpenCV untuk pemrosesan citra

# Membaca gambar dari file dengan format BGR (Blue, Green, Red)
img = cv.imread('../src/Photos/group 1.jpg')
cv.imshow('lady', img)  # menampilkan gambar asli

# Mengubah gambar dari BGR ke grayscale
# Haar Cascade membutuhkan input grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray lady', gray)

# Memuat model Haar Cascade (file XML berisi fitur deteksi wajah)
# Pastikan path file XML benar
haar_cascade = cv.CascadeClassifier('../Faces/haar_faces.xml')

# Mendeteksi wajah pada gambar grayscale
# scaleFactor : seberapa besar gambar di-resize pada setiap pencarian skala
# minNeighbors : seberapa banyak deteksi yang harus overlap untuk dianggap valid
faces_rect = haar_cascade.detectMultiScale(
    gray, 
    scaleFactor=1.1,
    minNeighbors=2
)

# Menampilkan jumlah wajah yang terdeteksi
print(f'Number of faces = {len(faces_rect)}')

# Menampilkan koordinat bounding box tiap wajah
# Format: (x posisi kiri, y posisi atas, width, height)
print(faces_rect)

# Loop setiap wajah yang terdeteksi
for (x,y,w,h) in faces_rect:
    # Menggambar persegi panjang pada posisi wajah
    # Warna biru (BGR: 255,0,0), ketebalan garis = 2
    cv.rectangle(img, (x,y), (x+w, y+h), (255,0,0), thickness=2)

# Menampilkan gambar yang sudah diberi bounding box wajah
cv.imshow('detected faces', img)

# Menunggu tombol keyboard sebelum program berhenti
cv.waitKey(0)

# ---------------------------------------------------------------
# RANGKUMAN:
# Kode ini melakukan deteksi wajah pada gambar menggunakan model
# Haar Cascade. Langkah-langkah utamanya:
# 1. Load gambar dan convert ke grayscale
# 2. Load file Haar Cascade (pre-trained classifier)
# 3. Mendeteksi lokasi wajah dengan detectMultiScale
# 4. Menggambar bounding box (kotak) di sekitar wajah
# 5. Menampilkan hasil deteksinya
#
# Intinya: program ini mendeteksi dan menandai wajah dalam gambar.
# ---------------------------------------------------------------

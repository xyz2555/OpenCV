import numpy as np
import cv2 as cv

# Load Haar Cascade untuk deteksi wajah (bukan recognition)
haar_cascade = cv.CascadeClassifier('../Faces/haar_faces.xml')

# List nama orang sesuai label numerik pada dataset training
people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']

# Jika ingin melihat fitur dan label asli yang digunakan saat training:
# features = np.load('features.npy')
# labels = np.load('labels.npy')

# Membuat object LBPH Recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Load model yang sudah dilatih sebelumnya
face_recognizer.read('../Faces/faces_trained.yml')

# Membaca gambar untuk pengujian / validasi
img = cv.imread(r'../src/Faces/val/jerry_seinfeld/2.jpg')

# Convert gambar ke grayscale (LBPH dan Haar membutuhkan grayscale)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)

# Deteksi wajah pada gambar menggunakan Haar Cascade
# scaleFactor=1.1 : parameter untuk memperbesar gambar pada setiap skala
# minNeighbors=4  : semakin besar, deteksi lebih ketat (mengurangi false positive)
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

# Loop untuk setiap wajah yang terdeteksi
for(x,y,w,h) in faces_rect:
    # Crop bagian wajah (ROI) berdasarkan koordinat bounding box
    faces_roi = gray[y:y+h, x:x+w]

    # Prediksi label dan confidence menggunakan LBPH
    # label: index dari array people
    # confidence: semakin kecil, prediksi semakin akurat
    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')

    # Tambahkan tulisan (nama orang) ke gambar output
    # Posisi teks diatur pada (20,20) dengan font dan warna hijau
    cv.putText(img, str(people[label]), (20,20),
               cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)

    # Menggambar kotak disekitar wajah yang terdeteksi
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

# Menampilkan gambar akhir dengan prediksi nama + bounding box
cv.imshow('Detected face', img)

# Menunggu input keyboard sebelum window ditutup
cv.waitKey(0)

# --------------------------------------------------------------
# RANGKUMAN:
# Kode ini melakukan face recognition (bukan hanya face detection):
# 1. Load model LBPH yang sudah dilatih (faces_trained.yml)
# 2. Baca gambar baru dan deteksi wajah dengan Haar Cascade
# 3. Crop wajah (ROI) dan lakukan prediksi label menggunakan LBPH
# 4. Tampilkan nama orang dan drawing bounding box di gambar
#
# Intinya: program ini mengidentifikasi siapa yang ada di dalam gambar
# berdasarkan model yang telah dilatih sebelumnya.
# --------------------------------------------------------------

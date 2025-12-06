import os                 # digunakan untuk mengakses file system (directory, file path)
import cv2 as cv          # OpenCV untuk pemrosesan citra dan face recognition
import numpy as np        # numpy untuk menyimpan data secara efisien

# Daftar nama orang (kelas) yang akan dilatih (label)
# Urutan list menentukan index label (0,1,2,...)
people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']

# Folder utama yang berisi subfolder untuk setiap orang
# Struktur folder harus seperti:
# ../src/Faces/train/Ben Afflek/
# ../src/Faces/train/Elton John/
# ...
DIR = r'../src/Faces/train/'

# Load classifier Haar Cascade untuk mendeteksi wajah
haar_cascade = cv.CascadeClassifier('../Faces/haar_faces.xml')

# List kosong untuk menyimpan data training
features = []    # list berisi region wajah (ROI)
labels = []      # list berisi label angka (misal 0,1,2,...)

# ----------------------------------------------------
# FUNGSI: melakukan scanning folder training, mendeteksi wajah, dan menyimpan ROI
# ----------------------------------------------------
def create_train():
    for person in people:             # loop setiap nama orang
        path = os.path.join(DIR, person)   # path subfolder person
        label = people.index(person)       # label angka berdasarkan index dalam list

        # Loop setiap file gambar dalam folder orang
        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)           # baca citra
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)  # convert grayscale

            # Deteksi wajah pada gambar
            faces_rect = haar_cascade.detectMultiScale(
                gray, scaleFactor=1.1, minNeighbors=3
            )

            # Untuk setiap wajah yang terdeteksi, potong ROI lalu simpan
            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]    # crop wajah (region of interest)
                features.append(faces_roi)        # simpan ROI ke fitur
                labels.append(label)              # simpan label numerik

# Memanggil fungsi untuk memproses dataset
create_train()
print('Training Done ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# Convert list ke numpy array
# dtype='object' karena setiap ROI memiliki dimensi berbeda (bervariasi ukuran)
features = np.array(features, dtype='object')
labels = np.array(labels)

# ----------------------------------------------------
# TRAINING MENGGUNAKAN LBP HISTOGRAM (LBPH FACE RECOGNIZER)
# ----------------------------------------------------

# Membuat model face recognizer (LBPH)
face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Training model menggunakan data ROI (features) dan labels
face_recognizer.train(features, labels)

# Menyimpan model yang sudah dilatih ke file .yml
face_recognizer.save('faces_trained.yml')

# Menyimpan data fitur dan label agar bisa digunakan tanpa train ulang
np.save('features.npy', features)
np.save('labels.npy', labels)

# ----------------------------------------------------
# RANGKUMAN:
# Code ini melakukan proses training sistem face recognition:
# 1. Membaca dataset gambar dari folder
# 2. Menggunakan Haar Cascade untuk mendeteksi wajah
# 3. Menyimpan potongan ROI wajah beserta labelnya
# 4. Melatih model LBPH (Local Binary Patterns Histogram)
# 5. Menyimpan model (.yml) dan data fitur (.npy) untuk penggunaan ke depannya
#
# Intinya:
# Program ini membangun database wajah dan melatih model pengenal wajah secara otomatis.
# ----------------------------------------------------

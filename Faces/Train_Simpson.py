# Install library (optional & hanya perlu dijalankan sekali)
# !pip install caer
# !pip install git+https://github.com/jasmcaus/canaro.git

import kagglehub  # library untuk mendownload dataset dari kaggle tanpa API

# Download dataset Simpsons dari Kaggle menggunakan KaggleHub
path = kagglehub.dataset_download("alexattia/the-simpsons-characters-dataset")

# Print lokasi tempat file dataset disimpan
print("Path to dataset files:", path)


import os              # untuk operasi file/directory
import caer            # library untuk data processing image (lebih simpel)
import canaro          # library untuk model CNN siap pakai
import numpy as np     # library matematika array
import cv2 as cv       # OpenCV untuk image processing
import gc              # garbage collector untuk membebaskan memory
import matplotlib.pyplot as plt  # untuk plotting / menampilkan image
from tensorflow.keras.utils import to_categorical # one-hot encoding label
from tensorflow.keras.preprocessing.image import ImageDataGenerator # augmentasi data
from tensorflow.keras.callbacks import LearningRateScheduler # scheduler learning rate


# Ukuran gambar input (80x80)
IMG_SIZE = (80, 80)

# Gunakan 1 channel (grayscale) agar training lebih ringan
channels = 1

# Path folder dataset karakter Simpsons
char_path = r'/root/.cache/kagglehub/datasets/alexattia/the-simpsons-characters-dataset/versions/4/simpsons_dataset'

# Dictionary untuk menyimpan jumlah gambar per karakter
char_dict = {}
for char in os.listdir(char_path):
    # Hitung jumlah gambar di folder setiap karakter
    char_dict[char] = len(os.listdir(os.path.join(char_path, char)))

# Sort karakter berdasarkan jumlah gambar, descending
char_dict = caer.sort_dict(char_dict, descending=True)
char_dict   # tampilkan dalam Jupyter


# Ambil hanya 10 karakter teratas (dengan gambar terbanyak)
characters = []
count = 0
for i in char_dict:
    characters.append(i[0])  # nama karakter
    count += 1
    if count >= 10:
      break
characters  # tampilkan list karakter


# Load dan preprocess semua gambar dari folder dataset
# agar siap untuk training
train = caer.preprocess_from_dir(
    char_path,           # path dataset
    characters,          # list karakter yang dipakai
    channels=channels,   # grayscale
    IMG_SIZE=IMG_SIZE,   # resize gambar
    isShuffle=True       # shuffle dataset
)

# Tampilkan jumlah total image yang berhasil di-load
len(train)


# Tampilkan contoh salah satu gambar
plt.figure(figsize=(30,30))
plt.imshow(train[0][0], cmap='gray')
plt.show()


# Pisahkan feature (X) dan label (y)
featureSet, labels = caer.sep_train(train, IMG_SIZE=IMG_SIZE)

# Normalisasi pixel agar 0-1
featureSet = caer.normalize(featureSet)

# Ubah label ke one-hot encoding (kategori)
labels = to_categorical(labels, len(characters))

# Split dataset ke train dan validation
x_train, x_val, y_train, y_val = caer.train_val_split(
    featureSet, labels, val_ratio=.2  # 20% val
)

# Hapus data yang tidak dibutuhkan dari RAM
del train
del featureSet
del labels
gc.collect()   # bersihkan memory


# Parameter training
BATCH_SIZE = 32
EPOCHS = 10

# Data augmentation untuk augmentasi training secara realtime
datagen = canaro.generators.imageDataGenerator()

# Generator batch training
train_gen = datagen.flow(x_train, y_train, batch_size=BATCH_SIZE)


# Buat model CNN dari library Canaro (sudah siap pakai)
model = canaro.models.createSimpsonsModel(
    IMG_SIZE=IMG_SIZE,
    channels=channels,
    output_dim=len(characters),         # jumlah kelas
    loss='binary_crossentropy',         # tipe loss
    decay=1e-6,                         # weight decay
    learning_rate=0.001,                # learning rate awal
    momentum=.9,                        # momentum SGD
    nesterov=True                       # gunakan nesterov momentum
)

# Tampilkan arsitektur model
model.summary()


# Learning rate scheduler untuk mengatur LR setiap epoch
callback_list = [LearningRateScheduler(canaro.lr_schedule)]


# Train model
training = model.fit(
    train_gen,                                     # data training
    steps_per_epoch=len(x_train)//BATCH_SIZE,      # jumlah step per epoch
    epochs=EPOCHS,                                 # jumlah epoch
    validation_data=(x_val, y_val),                # data validasi
    validation_steps=len(y_val)//BATCH_SIZE,       # step val
    callbacks = callback_list                      # scheduler LR
)


# Tampilkan list karakter lagi (urutan kelas)
characters


# Path ke contoh gambar untuk testing / prediksi single image
test_path = r'/root/.cache/kagglehub/datasets/alexattia/the-simpsons-characters-dataset/versions/4/kaggle_simpson_testset/kaggle_simpson_testset/bart_simpson_26.jpg'

# Load gambar test
img = cv.imread(test_path)

# Tampilkan gambar
plt.imshow(img, cmap='gray')
plt.show()


# Fungsi helper untuk preprocess gambar sebelum prediksi
def prepare(img):
  img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)     # grayscale
  img = cv.resize(img, IMG_SIZE)                # resize 80x80
  img = caer.reshape(img, IMG_SIZE, 1)          # reshape sesuai input CNN
  return img

# Prediksi gambar
predictions = model.predict(prepare(img))


# Tampilkan output raw prediction (probabilitas per kelas)
predictions

# Tampilkan nama karakter dengan probabilitas tertinggi
print(characters[np.argmax(predictions[0])])


# ----------------------------------------------------------
# RANGKUMAN PROGRAM INI:
#
# 1. Download dataset Simpsons menggunakan KaggleHub
# 2. Hitung jumlah gambar per karakter dan ambil 10 karakter terbanyak
# 3. Load semua gambar, resize, konversi grayscale, normalisasi
# 4. Split dataset ke train dan validation
# 5. Build model CNN menggunakan canaro
# 6. Latih model menggunakan data augmentation
# 7. Evaluasi model pada validation set
# 8. Prediksi satu gambar baru menggunakan model
# 9. Tampilkan karakter dengan probabilitas tertinggi
#
# Intinya:
# Notebook ini membangun dan melatih neural network
# untuk mengenali 10 karakter Simpsons dari dataset gambar.
# ----------------------------------------------------------

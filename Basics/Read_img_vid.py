import cv2 as cv   # Import library OpenCV dengan alias 'cv'

# Read images
img = cv.imread("../../src/Photos/cat_large.jpg")   # Membaca gambar dari path yang ditentukan

cv.imshow('Cat', img)   # Menampilkan gambar dengan nama jendela 'Cat'

cv.waitKey(0)   # Menunggu input tombol keyboard tanpa batas waktu agar jendela tidak langsung tertutup

# Read Videos
# capture = cv.VideoCapture("../../src/Videos/dog.mp4")   # Membuka file video dan membuat objek capture

# while True:   # Membuat loop agar video berjalan frame per frame
#     isTrue, frame = capture.read()   # Membaca frame dari video; isTrue=True jika berhasil, frame berisi data gambar
#     cv.imshow('Video', frame)        # Menampilkan frame video pada jendela bernama 'Video'

#     if cv.waitKey(20) & 0xff==ord('d'):   # Menunggu 20ms dan cek apakah tombol 'd' ditekan
#         break                            # Jika 'd' ditekan, keluar dari loop

# capture.release()    # Melepaskan resource video agar tidak terkunci sistem
# cv.destroyAllWindows()   # Menutup semua jendela yang dibuka OpenCV

# Kesimpulan:
# Program ini membaca video menggunakan OpenCV, menampilkannya frame demi frame,
# dan akan berhenti jika pengguna menekan tombol 'd'.

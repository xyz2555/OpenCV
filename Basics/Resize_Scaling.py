import cv2 as cv   

img = cv.imread('../src/Photos/cat_large.jpg')   
cv.imshow('Cat', img)   

def rescaleFrame(frame, scale=0.75):   # Fungsi untuk mengubah ukuran (resize) frame/gambar dengan faktor skala tertentu
    width = int(frame.shape[1] * scale)    # Hitung ulang lebar gambar sesuai skala
    height = int(frame.shape[0] * scale)   # Hitung ulang tinggi gambar sesuai skala
    dimension =  (width, height)           # Simpan ukuran baru dalam bentuk tuple (width, height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)   # Resize frame dengan metode interpolasi AREA

resized_image = rescaleFrame(img)   # Memanggil fungsi rescaleFrame untuk memperkecil gambar kucing
cv.imshow('Resized Image', resized_image)   # Menampilkan hasil gambar yang sudah di-resize

cv.waitKey(0)   

def changeRes(width,height):   # Fungsi untuk mengubah resolusi video secara langsung (khusus untuk video capture)
    capture.set(3, width)      # Properti ID 3 = lebar frame
    capture.set(4, height)     # Properti ID 4 = tinggi frame


capture = cv.VideoCapture("../src/Videos/dog.mp4")   

while True:   
    isTrue, frame = capture.read()   

    frame_resize = rescaleFrame(frame, scale=.4)   # Memperkecil ukuran frame video dengan skala 0.4

    cv.imshow('Video', frame)        
    cv.imshow('Video Resized', frame_resize)   # Menampilkan frame hasil resize dengan jendela berbeda

    if cv.waitKey(20) & 0xff==ord('d'):   
        break                            

capture.release()    
cv.destroyAllWindows()   

# Ringkasan:
# Program ini membaca gambar dan video, lalu menampilkan hasil aslinya dan versi yang telah diperkecil
# menggunakan fungsi rescaleFrame. Terdapat juga fungsi changeRes untuk mengatur resolusi video secara langsung.

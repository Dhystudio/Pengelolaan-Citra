#library opencv
import cv2
#Memanggil Gambar
imgrgb =cv2.imread("tommy.jpg")
#Transformasi Gambar RGB menjadi Grayscale
imggray = cv2.imread("tommy.jpg",0)
#Menampilkan Gambar RGB
cv2.imshow ("Gambar RGB",imgrgb)
#Menampilkan Gambar Grayscale
cv2.imshow ("Gambar Gray",imggray)
cv2.waitKey(0); cv2.destroyAllWindows()
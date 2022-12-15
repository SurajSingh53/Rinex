#edge detection
# types -- 1. sobel 2. laplacian 3. canny(most accurate)
import cv2
img = cv2.imread('New_Avengers_Vol_1_54_Textless.jpg',0)# 0 converts img to grayscale
sobel_x = cv2.Sobel(img,cv2.CV_8U,dx = 1,dy = 0,ksize = -1)
#cv_8u is unsigned 8bit/pixel
# kernel size(ksize) = -1 for edge detection
sobel_y = cv2.Sobel(img,cv2.CV_8U,dx= 0,dy = 1,ksize =-1)
# convolution is a matheatical way to combine 2 signals to create a third

sobel = cv2.bitwise_or(sobel_x,sobel_y)
cv2.imshow('Sobel X',sobel_x)
cv2.imshow('Sobel Y',sobel_y)
cv2.imshow('Sobel',sobel)

laplacian = cv2.Laplacian(img,cv2.CV_8U)
cv2.imshow('laplacian',laplacian)

canny = cv2.Canny(img,90,200)
cv2.imshow('Canny',canny)
cv2.waitKey(0)
cv2.destroyAllWindows()


# accuracy order -- canny > laplacian > sobel

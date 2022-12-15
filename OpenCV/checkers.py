import numpy as np
import cv2
img = np.zeros((300,300,3))
#creates a black background

     
    # print the pattern
for i in range(0,11):
    for j in range(0,9,2):
        if(i%2==0):
            img[(i*50):((i+1)*50),(j*50):((j+1)*50)]=255,255,255
        
        if(i%2==1):
            img[(i*50):((i+1)*50),((j+1)*50):((j+2)*50)] = 255,255,255
            
cv2.imshow('CHECKER BOARD',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

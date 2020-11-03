# Vincent Mai
# ECE 4554 - Computer Vision
# Sobel Filter and Canny Filter for Edge Detection for Problem 5, HW 2

import numpy as np
import cv2
import math
# Loading Grayscale of an Image
img = cv2.imread('boat.png', cv2.IMREAD_GRAYSCALE)
height = len(img)
width = len(img[0])

# Output Image
res = np.zeros((height, width,1), dtype= 'uint8')

# DETECT EDGE WITH SOBEL FILTER
x_sobel = np.array([[-1,0,1], [-2,0,2], [-1,0,1]])
y_sobel = np.array([[1,2,1], [0,0,0], [-1, -2, -1]])

for j in range(height - 3):
    for i in range(width - 3):
        gx = 2*img[j+1,i+1]+img[j+2,i]+img[j+2,i+2]-(2*img[j,i+1]+img[j,i]+img[j,i+2])
        gy =((2*img[j+1,i+2]+img[j,i+2]+img[j+2,i+2])-(2*img[j+1,i]+img[j,i]+img[j+2,i]));
        """
        for y in range(3):
            for x in range(3):
                gx += (x_sobel[y][x] * img[j + y -3][i + x -3])
                gy += (y_sobel[y][x] * img[j + y - 3][i + x -3])
                
        """
        
        gx = abs(gx) * .5
        gy = abs(gy) * .5
        gradient = math.sqrt(gx**2 + gy**2)
        res[j][i] = gradient

# CANNY EDGE DETECTION
res2 = cv2.Canny(img,50, 250)
 
# Show image at 1/2 scale
cv2.namedWindow('INPUT')
cv2.imshow('INPUT', img)
cv2.imshow('SOBEL', res)
cv2.imshow('CANNY', res2)
cv2.imwrite('outputP5Sobel.png', res)
cv2.imwrite('outputP5Canny.png', res2)
cv2.waitKey(0)
cv2.destroyAllWindows()



import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('dunk.png',0)

laplacian = cv2.Laplacian(img,cv2.CV_64F)
cv2.imwrite('dunkPlacian.png',laplacian)

cv2.imshow('image',laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()
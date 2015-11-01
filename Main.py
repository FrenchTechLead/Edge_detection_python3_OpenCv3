
import cv2
import numpy as np
from Edge.Sobel import *
from Edge.Hough import *


img = cv2.imread('dunk.png') # importing in grayScale Mode

imgSobel = mySobel(img, 1)

linedImageObject = Hough(imgSobel,img, 0.4)

linedImage = linedImageObject.drawLines()




cv2.imshow('linedImage', linedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
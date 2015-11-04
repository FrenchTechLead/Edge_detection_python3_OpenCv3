import math
import cv2
import numpy as np
from Edge.Sobel import *
from Edge.Hough import *
from Edge.ImageProp import *

def nothing(x):
    pass

inputImage = cv2.imread('dunk.jpg')
imgProp = ImageProp(inputImage) # just getting image resolution and diagonal

imgSobel = mySobel(inputImage, 1) # second parameter refers to ksize
cv2.imshow('Sobel', imgSobel)

a = imgProp.diagonal


cv2.namedWindow('parametres')

cv2.createTrackbar('Threshold', 'parametres', a, math.floor(a/2), nothing)
cv2.createTrackbar('MinLineLenth', 'parametres', a, math.floor(a/2), nothing)
cv2.createTrackbar('MaxLineGape', 'parametres', a, math.floor(a/2), nothing)

while(1):

    k = cv2.waitKey(1) & 0xFF
    if k == 27: # press escape to stop looping
        break
    # get current positions of four trackbars
    threshold = cv2.getTrackbarPos('Threshold','parametres')
    minLineLenth = cv2.getTrackbarPos('MinLineLenth','parametres')
    maxLineGape = cv2.getTrackbarPos('MaxLineGape','parametres')


    inputImage = cv2.imread('dunk.jpg')
    linedImageObject = Hough(imgSobel,inputImage, 0.25)# third parameter refers to Threashold Coef
    returnedArray = linedImageObject.drawLinesP( minLineLenth, maxLineGape,inputImage,threshold)
    inputImage = returnedArray[0]

    cv2.imshow('parametres', inputImage)

cv2.waitKey(0)

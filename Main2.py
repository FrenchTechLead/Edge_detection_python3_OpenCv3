__author__ = 'root'

import cv2
import math
import numpy as np
from Edge.Sobel import *
from Edge.Hough import *

def nothing(x):
    pass
inputImage = cv2.imread('dunk.png')
inputImage1 = cv2.imread('dunk.png')
cv2.namedWindow('fenetre')

cv2.createTrackbar('Threshold','fenetre',100,25,nothing)


switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'fenetre',1,1,nothing)

imgSobel = mySobel(inputImage, 1) # second parameter refers to ksize


threshold = 0
minLineLenth = 0
maxLineGape = 0
while(1):

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    # get current positions of four trackbars
    threshold = cv2.getTrackbarPos('Threshold','fenetre')

    s = cv2.getTrackbarPos(switch,'fenetre')



    if s == 0:
        break
    else:
        inputImage1 = cv2.imread('dunk.png')
        linedImageObject = Hough(imgSobel,inputImage1,  math.floor(threshold/1000))# third parameter refers to Threashold Coef
        linedImage = linedImageObject.drawLines()
        cv2.imshow('fenetre', linedImage)
        cv2.imshow('Sobel', imgSobel)
        cv2.imshow('inputImage1', inputImage1)
        cv2.imshow('inputImage', inputImage)

cv2.waitKey(0)

import math
import cv2
import numpy as np
from Edge.Sobel import *
from Edge.Hough import *
from Edge.ImageProp import *
from Edge.LinesHandler import *

def nothing(x):
    pass
print("Welcome to Python WhiteBoard Recognition Program\n\n"
      "Since images dont have  the same proprieties, the parameteres of the whiteBoard detection program are not  the same for two images \n"
      "That's why you need to use the TrackBars to find the perfect parameteres for your inputImage \n\n"
      "press C when you perfectly detect edges")

inputImage = cv2.imread('dunk.jpg')
imgProp = ImageProp(inputImage) # just getting image resolution and diagonal

imgSobel = mySobel(inputImage, 1) # second parameter refers to ksize
cv2.imshow('Sobel', imgSobel)

a = imgProp.diagonal


cv2.namedWindow('parametres')

cv2.createTrackbar('Threshold', 'parametres', a, math.floor(a/2), nothing)
cv2.createTrackbar('MinLineLenth', 'parametres', 0, math.floor(a/2), nothing)
cv2.createTrackbar('MaxLineGape', 'parametres', 0, math.floor(a/2), nothing)

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
    lines = returnedArray[1]

    if k == ord('c'):
        print("all points :")
        print(lines)
        linesHandler = LinesHandler(lines, imgProp.width, imgProp.height)
        linesHandler.split()
        points = linesHandler.getPoints()
        cv2.circle(inputImage,points[0], 10, (50,255,255), -1)
        cv2.circle(inputImage,points[1], 10, (50,255,255), -1)
        cv2.circle(inputImage,points[2], 10, (50,255,255), -1)
        cv2.circle(inputImage,points[3], 10, (50,255,255), -1)
        cv2.imshow('parametres', inputImage)
        break



cv2.waitKey(0)

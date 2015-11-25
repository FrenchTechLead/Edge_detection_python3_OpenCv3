import math
import cv2
import numpy as np
from Edge.Sobel import *
from Edge.Hough import *
from Edge.ImageProp import *
from Edge.LinesHandler import *



inputImage = cv2.imread('dunk.png')
imgProp = ImageProp(inputImage) # just getting image resolution and diagonal

imgSobel = mySobel(inputImage, 3) # second parameter refers to ksize

a = imgProp.diagonal

minLineLenth = math.floor(a /2)
maxLineGape =  math.floor(a/50)
threshold = math.floor(a /2)

linedImageObject = Hough(imgSobel,inputImage)# third parameter refers to Threashold Coef
returnedArray = linedImageObject.drawLinesP( minLineLenth, maxLineGape,inputImage,threshold)
inputImage = returnedArray[0]
cv2.imshow('parametres', inputImage)
lines = returnedArray[1]

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

pts1 = np.float32([points[0],points[1],points[2],points[3]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(inputImage,M,(300,300))

cv2.imshow('output', dst)

cv2.waitKey(0)

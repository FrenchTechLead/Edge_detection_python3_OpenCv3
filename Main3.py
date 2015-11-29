import math
from distutils.command.install import install

import cv2
import numpy as np
from Edge.Sobel import *
from Edge.Hough import *
from Edge.ImageProp import *
from Edge.LinesHandler import *




inputImage = cv2.imread('24.jpg')
inputImage2 = cv2.imread('24.jpg')
imgProp = ImageProp(inputImage) # just getting image resolution and diagonal
a = imgProp.diagonal

if( a > 1200):
    inputImage = cv2.resize(inputImage, (800, 600))
    inputImage2 = cv2.resize(inputImage2, (800, 600))
    imgProp = ImageProp(inputImage) # just getting image resolution and diagonal
    a = imgProp.diagonal

imgSobel = mySobel(inputImage, 3) # second parameter refers to ksize



minLineLenth = math.floor(a*0.4)
maxLineGape = math.floor(50)
threshold = math.floor(a*0.4)

linedImageObject = Hough(imgSobel, inputImage)
returnedArray = linedImageObject.drawLinesP(minLineLenth, maxLineGape, inputImage, threshold)
inputImage = returnedArray[0] #retourne l image avec les lignes vertes

lines = returnedArray[1] # retourne les segments de lignes

print("all points :")
print(lines)

linesHandler = LinesHandler(lines, imgProp.width, imgProp.height)

linesHandler.split()# decoupe l image en 4 morceaux egaux

points = linesHandler.getPoints()
cv2.circle(inputImage, points[0], 10, (50, 255, 255), -1)
cv2.circle(inputImage, points[1], 10, (50, 255, 255), -1)
cv2.circle(inputImage, points[2], 10, (50, 255, 255), -1)
cv2.circle(inputImage, points[3], 10, (50, 255, 255), -1)

cv2.imshow('parametres', inputImage)

length = linesHandler.getLongestLine()
width = math.floor(0.75*length)
pts1 = np.float32([points[0], points[1], points[2], points[3]])
pts2 = np.float32([[0, 0], [length, 0], [0, width], [length, width]])

M = cv2.getPerspectiveTransform(pts1, pts2)

dst = cv2.warpPerspective(inputImage2, M, (length, width))

cv2.imshow('output', dst)
print(linesHandler.getLongestLine())
cv2.waitKey(0)

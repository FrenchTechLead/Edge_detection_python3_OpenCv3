import cv2
import math
import numpy as np

class Hough:

    diagonalOfImage = 0
    coefThreshold = 0
    threshold = 0
    def __init__(self, imgBW, imgColor, coefThreshold ):
        """
        Constructeur de l objet Hough.
        """
        self.inputImageBW = imgBW
        inputImageColor = imgColor
        self.coefThreshold = coefThreshold
        self.height, self.width = imgColor.shape[:2] # getting the image proprieties
        self.diagonalOfImage = math.sqrt(self.height**2 + self.width**2)
        self.threshold = math.floor(self.diagonalOfImage*self.coefThreshold)


    def drawLines(self):

        lines = cv2.HoughLines(self.inputImageBW, 1, np.pi/180, math.floor(self.diagonalOfImage*self.coefThreshold))

        for i in range(len(lines)):

            for rho, theta in lines[i-1]:
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a*rho
                y0 = b*rho
                x1 = int(x0 + self.diagonalOfImage*(-b))
                y1 = int(y0 + self.diagonalOfImage*(a))
                x2 = int(x0 - self.diagonalOfImage*(-b))
                y2 = int(y0 - self.diagonalOfImage*(a))

                print("x1 = "+str(x1)+" y1 = "+str(y1))
                print("x2 = "+str(x2)+" y2 = "+str(y2)+"\n")
                cv2.line(self.inputImageColor, (x1, y1), (x2, y2), (0, 0, 255), 1)
        return self.inputImageColor

    def drawLinesP(self, minLineLenght, maxLineGap, coloredImage, thresholdOptional = threshold):
        lines = cv2.HoughLinesP(self.inputImageBW,1,np.pi/180,thresholdOptional,minLineLenght, maxLineGap)
        for i in range(len(lines)):
            for x1,y1,x2,y2 in lines[i-1]:
                cv2.line(coloredImage, (x1, y1), (x2, y2),(0,255,0),1)
                #print("x1 = "+str(x1)+" y1 = "+str(y1))
                #print("x2 = "+str(x2)+" y2 = "+str(y2)+"\n")
                #print(self.threshold)
                print("minLineLenght = "+str(minLineLenght)+" maxLineGap = "+str(maxLineGap)+" threshold = "+str(thresholdOptional))
        return coloredImage
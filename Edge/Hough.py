import cv2
import math
import numpy as np

class Hough:

    diagonalOfImage = 0

    threshold = 0
    def __init__(self, imgBW, imgColor ):
        """
        Constructeur de l objet Hough.
        """
        self.inputImageBW = imgBW
        inputImageColor = imgColor
        self.height, self.width = imgColor.shape[:2] # getting the image proprieties
        self.diagonalOfImage = math.sqrt(self.height**2 + self.width**2)



    def drawLinesP(self, minLineLenght, maxLineGap, coloredImage, threshold):
        lines = cv2.HoughLinesP(self.inputImageBW,1,np.pi/180,threshold,minLineLenght, maxLineGap)
        print(lines)
        for i in range(len(lines)):
            for x1,y1,x2,y2 in lines[i-1]:
                cv2.line(coloredImage, (x1, y1), (x2, y2),(0,255,0),1)
                # print("x1 = "+str(x1)+" y1 = "+str(y1))
                #print("x2 = "+str(x2)+" y2 = "+str(y2)+"\n")

                #print("minLineLenght = "+str(minLineLenght)+" maxLineGap = "+str(maxLineGap)+" threshold = "+str(thresholdOptional))
        return [coloredImage, lines]
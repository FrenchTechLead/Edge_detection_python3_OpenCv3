import cv2
import math
import numpy as np

class Hough:

    diagonalOfImage = 0
    coefThreshold = 0

    def __init__(self, imgBW, imgColor, coefThreshold ):
        """
        Constructeur de l objet Hough.
        """
        self.inputImageBW = imgBW
        self.inputImageColor = imgColor
        self.coefThreshold = coefThreshold
        self.height, self.width = imgColor.shape[:2]
        self.diagonalOfImage = math.sqrt(self.height**2 + self.width**2)



    def drawLines(self):

        lines = cv2.HoughLines(self.inputImageBW, 1, np.pi/180, math.floor(self.diagonalOfImage*self.coefThreshold))

        for i in range(len(lines)):

            for rho, theta in lines[i-1]:
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a*rho
                y0 = b*rho
                x1 = int(x0 + 1599*(-b))
                y1 = int(y0 + 1599*(a))
                x2 = int(x0 - 1599*(-b))
                y2 = int(y0 - 1599*(a))

                cv2.line(self.inputImageColor, (x1, y1), (x2, y2), (0, 0, 255), 1)
        return self.inputImageColor
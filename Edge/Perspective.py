import math
import numpy as np
import cv2
class Perspective:



    def __init__(self, inputImage, points, longestLine ):
        """
        Constructeur de l objet Perspective.
        """
        self.inputImage = inputImage

        self.length = longestLine
        self.width = math.floor(0.75*self.length)
        self.pnts1 = np.float32([points[0], points[1], points[2], points[3]]) # cordonnées du qudrilatere
        self.pnts2 = np.float32([[0, 0], [self.length, 0], [0, self.width], [self.length, self.width]]) # cordonnées du tableau dan sla nouvelle image


    def get(self):

        M = cv2.getPerspectiveTransform(self.pnts1, self.pnts2)
        dst = cv2.warpPerspective(self.inputImage, M, (self.length, self.width))

        return dst




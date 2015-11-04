import cv2
import math
import numpy as np


class ImageProp:
    diagonal = 0
    height = 0
    width = 0

    def __init__(self, img):
        self.height, self.width = img.shape[:2] # getting the image proprieties
        self.diagonal  = math.floor(math.sqrt(self.height**2 + self.width**2))
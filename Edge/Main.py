__author__ = 'root'
import cv2
import numpy as np
import Sobel


img = cv2.imread('dunk.jpg')

img = sobel(img, 3)
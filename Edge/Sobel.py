__author__ = 'root'
import cv2
import numpy as np

ddepth = cv2.CV_16S



def mySobel( inputImage, ksize):
    img = cv2.GaussianBlur(inputImage, (3, 3), 0) #noise suppression
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # conversion to grayScale
    img = cv2.equalizeHist(img) # egalisation de l histogramme pour mieux detecter les contours
    grad_x = cv2.Sobel(img, ddepth, 1, 0, ksize=ksize, borderType=cv2.BORDER_DEFAULT)# Gradient-X
    grad_y = cv2.Sobel(img, ddepth, 0, 1, ksize=ksize, borderType=cv2.BORDER_DEFAULT)# Gradient-Y
    sobxImage = cv2.convertScaleAbs(grad_x)# conversion to uint8
    sobyImage = cv2.convertScaleAbs(grad_y)# conversion to uint8
    mergedImage = cv2.addWeighted(sobxImage, 2, sobyImage, 2, 0) # fusion of sobx and soby
    (thresh, im_bw) = cv2.threshold(mergedImage, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)# to black and white

    return im_bw
import cv2
import numpy as np
import math
scale = 1
delta = 0
ddepth = cv2.CV_16S

img = cv2.imread('dunk.png')
height, width = img.shape[:2]
maxMesure = max(height, width)
coefThreshold = 0.5

img = cv2.GaussianBlur(img, (3, 3), 0) #noise suppression
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # conversion to grayScale

# Gradient-X
grad_x = cv2.Sobel(gray, ddepth, 1, 0, ksize=3, borderType=cv2.BORDER_DEFAULT)


# Gradient-Y
grad_y = cv2.Sobel(gray, ddepth, 0, 1, ksize=3, borderType=cv2.BORDER_DEFAULT)


sobxImage = cv2.convertScaleAbs(grad_x)   # conversion to uint8
sobyImage = cv2.convertScaleAbs(grad_y)


mergedImage = cv2.addWeighted(sobxImage, 2, sobyImage, 2, 0) # fusion of sobx and soby


(thresh, im_bw) = cv2.threshold(mergedImage, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)# to black and white
cv2.imshow('im_bw',im_bw)

lines = cv2.HoughLines(im_bw, 1, np.pi/180,math.floor(maxMesure*coefThreshold))

for i in range(len(lines)):
    print(lines[i])
    for rho, theta in lines[i-1]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1599*(-b))
        y1 = int(y0 + 1599*(a))
        x2 = int(x0 - 1599*(-b))
        y2 = int(y0 - 1599*(a))

        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.imshow('img', img)


cv2.waitKey(0)
cv2.destroyAllWindows()
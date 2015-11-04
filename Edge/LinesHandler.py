import numpy as np

class LinesHandler:

    lines =[[ [0]]]
    h = 0
    w = 0

    def __init__(self, lines, height, width ):
         """
         This class splits the image to 4 equal parts, assuming that each part of the image contains one corner of the table
         we'll try to find each corner.
         :param lines:
         :param height:
         :param width:
         :return:
         """
         self.lines = lines
         self.h = height
         self.w = width

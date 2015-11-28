import numpy as np
import math
class LinesHandler:

    lines =[[ [0]]]
    h = 0
    w = 0
    partOneList = []
    partTwoList = []
    partThreeList = []
    partFourList = []
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
         self.partOneList = []
         self.partTwoList = []
         self.partThreeList = []
         self.partFourList = []


    def split(self):

        for i in range(len(self.lines)):
            for x1, y1, x2, y2 in self.lines[i-1] :

                if (x1 < math.floor(self.w/2) and y1 < math.floor(self.h/2)):
                    self.partOneList.append((x1, y1))
                if (x1 > math.floor(self.w/2) and y1 < math.floor(self.h/2)):
                    self.partTwoList.append((x1, y1))
                if (x1 < math.floor(self.w/2) and y1 > math.floor(self.h/2)):
                    self.partThreeList.append((x1, y1))
                if (x1 > math.floor(self.w/2) and y1 > math.floor(self.h/2)):
                    self.partFourList.append((x1, y1))

                if (x2 < math.floor(self.w/2) and y2 < math.floor(self.h/2)):
                    self.partOneList.append((x2, y2))
                if (x2 > math.floor(self.w/2) and y2 < math.floor(self.h/2)):
                    self.partTwoList.append((x2, y2))
                if (x2 < math.floor(self.w/2) and y2 > math.floor(self.h/2)):
                    self.partThreeList.append((x2, y2))
                if (x2 > math.floor(self.w/2) and y2 > math.floor(self.h/2)):
                    self.partFourList.append((x2, y2))

        return [self.partOneList, self.partTwoList, self.partThreeList, self.partFourList ]


    def getPoints(self):

        moX1= 0
        moY1= 0
        moX2= 0
        moY2= 0
        moX3= 0
        moY3= 0
        moX4= 0
        moY4= 0
        print()
        print("spliters")
        print(math.floor(self.w/2))
        print(math.floor(self.h/2))
        print()


        print("part one list")
        print(self.partOneList)
        for x1,y1 in self.partOneList:
            moX1 = moX1 +x1
            moY1 = moY1 +y1
        moX1 = math.floor(moX1/len(self.partOneList))
        moY1 = math.floor(moY1/len(self.partOneList))
        print(moX1)
        print(moY1)

        print()

        print("part two list")
        print(self.partTwoList)
        for x2,y2 in self.partTwoList:
            moX2 = moX2 +x2
            moY2 = moY2 +y2
        moX2 = math.floor(moX2/len(self.partTwoList))
        moY2 = math.floor(moY2/len(self.partTwoList))
        print(moX2)
        print(moY2)



        print()

        print("part three list")
        print(self.partThreeList)
        for x3,y3 in self.partThreeList:
            moX3 = moX3 +x3
            moY3 = moY3 +y3
        moX3 = math.floor(moX3/len(self.partThreeList))
        moY3 = math.floor(moY3/len(self.partThreeList))
        print(moX3)
        print(moY3)

        print()

        print("part four list")
        print(self.partFourList)
        for x4,y4 in self.partFourList:
            moX4 = moX4 +x4
            moY4 = moY4 +y4
        moX4 = math.floor(moX4/len(self.partFourList))
        moY4 = math.floor(moY4/len(self.partFourList))
        print(moX4)
        print(moY4)
        print()

        return [(moX1, moY1), (moX2, moY2), (moX3, moY3), (moX4, moY4)]

    def getLongestLine(self,):
        length =0
        for i in range(len(self.lines)):
            for x1, y1, x2, y2 in self.lines[i-1] :

                d = math.floor( math.sqrt( (x1-x2)**2 + (y1-y2)**2 ) )
                if (d > length): length = d
        return length
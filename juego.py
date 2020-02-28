
'sudo pip install opencv-contrib-python'

import cv2
import matplotlib
import numpy as np

import random
from random import seed
from random import randint

limiteMax = 100
n = 0
b = 255


def checkCellLives(img,x,y):
    cellLives = 0
    'check x+1 cell'
    try:
        if img[x+1][y] == n:
            cellLives +=1
        pass
    except IndexError:
        pass
    'check x-1 cell'
    try:
        if img[x-1][y] == n:
            cellLives +=1
        pass
    except IndexError:
        pass
    'check y+1 cell'
    try:
        if img[x][y+1] == n:
            cellLives +=1
        pass
    except IndexError:
        pass
    'check y-1 cell'
    try:
        if img[x][y-1] == n:
            cellLives +=1
        pass
    except IndexError:
        pass
    pass
    'check x+1/y-1 cell'
    try:
        if img[x+1][y-1] == n:
            cellLives +=1
        pass
    except IndexError:
        pass
    pass
    'check x+1/y+1 cell'
    try:
        if img[x+1][y+1] == n:
            cellLives +=1
        pass
    except IndexError:
        pass
    pass
    'check x-1/y-1 cell'
    try:
        if img[x-1][y-1] == n:
            cellLives +=1
        pass
    except IndexError:
        pass
    pass
    'check x-1/y+1 cell'
    try:
        if img[x-1][y+1] == n:
            cellLives +=1
        pass
    except IndexError:
        pass
    return cellLives

img = np.zeros((limiteMax, limiteMax, 1), dtype = "uint8")

print('Press Ctrl-C to quit.')
try:
    for x in range(len(img)):
        for y in range(len(img)):
            img[x][y] = b
            pass
        pass
    'Initialize enviroment'
    start = 0
    while start < 400:
        x = randint(0,limiteMax-1)
        y = randint(0,limiteMax-1)
        img[x,y] = n
        start+=1
    while True:
        #x = randint(0,limiteMax-1)
        #y = randint(0,limiteMax-1)
        for x in range(len(img)):
            for y in range(len(img)):
                if img[x][y] == n:
                    cellLives = checkCellLives(img,x,y)
                    print(cellLives)

                    if cellLives == 2:
                        img[x][y] = n
                    elif cellLives == 3:
                        img[x][y] = n
                    else:
                        img[x][y] = b
                elif img[x][y] == b:
                    cellLives = checkCellLives(img,x,y)
                    print(cellLives)

                    if cellLives == 3:
                        img[x][y] = n
                    else:
                        img[x][y] = b
                    pass
                else:
                    img[x][y] = b

        totalCellLives = 0
        for x in range(len(img)):
            for y in range(len(img)):
                if img[x][y] == n:
                    totalCellLives += 1
                pass
            pass
        if totalCellLives == 0:
            print("Enviroment Fail!")
            cv2.namedWindow('image',10)
            cv2.resizeWindow('image', 600,600)
            cv2.imshow('image',img)
            cv2.waitKey(0)
            input()
            break
        else:
            cv2.namedWindow('image',10)
            cv2.resizeWindow('image', 600,600)
            cv2.imshow('image',img)
            cv2.waitKey(1)
except KeyboardInterrupt:
    print('\n')

#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
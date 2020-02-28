"""
Title: The Game of Life
Author: John Horton Conway

The Game of Life, also known simply as Life, is a cellular
automaton devised by the British mathematician John Horton Conway in 1970.

The game is a zero-player game, meaning that its evolution is determined by
its initial state, requiring no further input. One interacts with the Game of
Life by creating an initial configuration and observing how it evolves. It is
Turing complete and can simulate a universal constructor or any other Turing machine.
Source: (https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)

This code to use is necesary install opencv to python, in Fedora :
    sudo pip install opencv-contrib-python
"""

import cv2
import matplotlib
import numpy as np

import random
from random import seed
from random import randint

limiteMax = 100
checkMax = 10
checkMin = 10

n = 1
b = 255

def checkCellLives(img,x,y):
    cellLives = 0
    'check x+1 cell'
    if img[x+1][y] == n:
        cellLives +=1
    'check x-1 cell'
    if img[x-1][y] == n:
        cellLives +=1
    'check y+1 cell'
    if img[x][y+1] == n:
        cellLives +=1
    'check y-1 cell'
    if img[x][y-1] == n:
        cellLives +=1
    'check x+1/y-1 cell'
    if img[x+1][y-1] == n:
        cellLives +=1
    'check x+1/y+1 cell'
    if img[x+1][y+1] == n:
        cellLives +=1
    'check x-1/y-1 cell'
    if img[x-1][y-1] == n:
        cellLives +=1
    'check x-1/y+1 cell'
    if img[x-1][y+1] == n:
        cellLives +=1
    return cellLives

img = np.zeros((limiteMax, limiteMax, 1), dtype = "uint8")

print('Press Ctrl-C to quit.')
try:
    cv2.namedWindow('image',10)
    cv2.resizeWindow('image', 800,800)

    for x in range(1,len(img)-1):
        for y in range(1,len(img)-1):
            img[x][y] = b
            pass
        pass
    print('Initialize enviroment')
    start = 0
    while start < 4:
        x = randint(checkMin,limiteMax-checkMax)
        y = randint(checkMin,limiteMax-checkMax)
        cv2.circle(img, (x,y), 4, n, thickness=1, lineType=8, shift=0)
        cv2.circle(img, (randint(checkMin,limiteMax-checkMax),y), 3, n, thickness=1, lineType=8, shift=0)
        cv2.circle(img, (x,randint(checkMin,limiteMax-checkMax)), 1, n, thickness=1, lineType=8, shift=0)
        start+=1

    while True:
        for x in range(checkMin,len(img)-checkMax):
            for y in range(checkMin,len(img)-checkMax):
                if img[x][y] == n:
                    cellLives = checkCellLives(img,x,y)
                    if cellLives == 2 or  cellLives == 3:
                        img[x][y] = n
                    else:
                        img[x][y] = b
                elif img[x][y] == b:
                    cellLives = checkCellLives(img,x,y)
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
            cv2.imshow('image',img)
            cv2.waitKey(0)
            input()
            break
        else:
            print("Run...")
            cv2.imshow('image',img)
            cv2.waitKey(4)
except KeyboardInterrupt:
    print('\n')

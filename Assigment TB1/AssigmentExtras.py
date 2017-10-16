# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 19:53:52 2017

@author: Gabriel PC
"""

import numpy as np
import cv2
import time
from matplotlib import pyplot as plt

#extra
def cargar(link): #Load picture
    img  = cv2.imread(link)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    return img

def show(temp): #Used to show the picture
    plt.imshow(temp)
    plt.show()
    return

def to_gray(image):
    img = np.copy(image)
    img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    return img

def back_gray(image):
    img = np.copy(image)
    img = cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
    return img

def floyd_steinberg(image,tipo): #1 normal, 2 serpent
    img = np.copy(image)
    sx,sy = np.size(image,0) - 1,np.size(image,1) - 1
    ran = [0,sy-1]
    for i in range(0,sx):
        for j in range(ran[0],ran[1]):
            temp_pixel = img[i][j]
            npixel = round(temp_pixel/255)*255 #Threshold
            img[i][j] = npixel
            error = temp_pixel - npixel
            img[i+1][j] = min(255,img[i + 1][j] + error * 7/16)
            img[i-1][j+1] = min(255,img[i-1][j+1] + error * 3/16)
            img[i][j+1] = min(255,img[i][j+1] + error * 5 / 16)
            img[i+1][j+1] = min(255,img[i+1][j+1] + error / 16)
        if(tipo == 2): ran.reverse()
    return img


def demo3():
    trial = cargar("test2.jpg")
    ktrial = to_gray(trial)
    nasd = floyd_steinberg(ktrial,2)
    final = back_gray(nasd)
    show(final)
    cv2.imwrite("result.jpg",final)
    pass
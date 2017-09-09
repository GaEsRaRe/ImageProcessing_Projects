#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 20:05:45 2017

@author: gramirez
"""

import cv2
from matplotlib import pyplot as plt
import numpy as np
import random as rd


matrix = [[0.299, 0.587, 0.111],
          [0.596,-0.274,-0.322],
          [0.211,-0.523, 0.321]]

matrix2 = [[1, 0.956, 0.621],
           [1,-0.272,-0.647],
           [1,-1.106, 1.703]]

def cargar(link): #Load picture
    img  = cv2.imread(link)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    return img

def convert(base,option): #option1  RGB 2 YIQ and option2 YIQ to RGB
    image = np.copy(base)
    sizex = np.size(image,0) 
    sizey = np.size(image,1)
    if (option == 1):
        for i in range(0,sizex):
            for j in range(sizey):
                temp = [image[i][j][0],image[i][j][1],image[i][j][2]]
                new = np.dot(matrix,temp)
                #print(new)
                image[i][j] = new
    if (option == 2):
        for i in range(0,sizex):
            for j in range(sizey):
                temp = [image[i][j][0],image[i][j][1],image[i][j][2]]
                new = np.dot(matrix2,temp)
                image[i][j] = float(new)
        
   
    #img []
    
    return image

def convert_working(image):
    result = np.copy(image)
    
    result = cv2.cvtColor(result,cv2.COLOR_RGB2HSV)
    sizex = np.size(result,0) 
    sizey = np.size(result,1)
    for i in range(0,sizex):
        for j in range(sizey):
            result[i][j][2] = min(255,result[i][j][2] *1.2)
    result = cv2.cvtColor(result,cv2.COLOR_HSV2RGB)
    show(result)
    return result 

def intensity(image): #need to be converted
    img = np.copy(image)
    sizex = np.size(img,0) 
    sizey = np.size(img,1)
    for i in range(0,sizex):
        for j in range(sizey):
            img[i][j][1] = min(255,img[i][j][1] * 1.2)
    
    
    return img

def show(temp):
    plt.imshow(temp)
    plt.show()
    return
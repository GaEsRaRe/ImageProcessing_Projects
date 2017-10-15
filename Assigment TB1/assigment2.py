# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 15:24:20 2017

@author: Gabriel PC
"""

#asigment 2

import numpy as np
import random as rd
import cv2
from matplotlib import pyplot as plt

#Basic Functions 

def cargar(link): #Load picture
    img  = cv2.imread(link)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    return img

def show(temp): #Used to show the picture
    plt.imshow(temp)
    plt.show()
    return

def to_grey(image):
    img = np.copy(image)
    img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    return img

def back_grey(image):
    img = np.copy(image)
    img = cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
    return img

def join_same_size(image1,image2,a,b): #both images and the % of each one
    sx, sy = np.size(image1,0),np.size(image1,1)
    img = np.copy(image1)
    for i in range(0,sx):
        for j in range(0,sy):
            img[i][j] = max(0,min(255,image1[i][j]*a + image2[i][j]*b))
            
    return img

def join(image1,image2,a,b):
    s1x,s1y = np.size(image1,0),np.size(image1,1)
    s2x,s2y = np.size(image1,0),np.size(image1,1)
    if(s1x == s2x and s1y == s2y):
        img = join_same_size(image1,image2,a,b)
    if(s1x > s2x and s1y > s2y):
        img = join_same_size(image1,image2,a,b)
    if(s1x < s2x and s1y < s2y):
        img = join_same_size(image2,image1,b,a)
    
    return img
def demo():
    img1 = cargar("b1.jpg")
    img2 = cargar("b2.jpg")
    img1 = to_grey(img1)
    img2 = to_grey(img2)
    img = join(img1,img2,0.5,0.5)
    img = back_grey(img)
    show(img)
    cv2.imwrite("lala.png",img)
    return 
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 14:46:31 2017

@author: gramirez
"""

#Project for the course of Image Procesing UPC 2017-2


import cv2
from matplotlib import pyplot as plt
import numpy as np
import random as rd


def cargar(link): #Load picture
    img  = cv2.imread(link)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    return img

def show(temp):
    plt.imshow(temp)
    plt.show()
    return

def empty():
    matrix = []
    for i in range(0,255):
        matrix.append(0)
    
    return matrix


"""
def entriophy(img):
    sizex = np.size(img,0) 
    sizey = np.size(img,1)
    contador = 0
    for i in range(0,sizex):
        for j in range(0,sizey):    
            
        
    return
"""
def GreyScale(img): #Load picture
    img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    plt.imshow(img,cmap='gray')
    return img

def empty_image(img):
    image = np.zeros_like(img)
    return image

def Girar(img):
    None
    return 
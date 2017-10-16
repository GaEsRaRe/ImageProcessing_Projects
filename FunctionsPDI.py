# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 16:31:45 2017

@author: Gabriel PC
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt 
#FunctionsPDI.py

def cargar(direccion):
    img = cv2.imread(direccion) #cargamos la imagen de la  direccion dada
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #convertimos la imagen de BGR a RGB
    
    return img

def show(imagen):
    plt.imshow(imagen) #Cargamos la imagen en el plot
    plt.show() #Mostramos el plot
    pass

def to_gray(image):
    img = np.copy(image)
    img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    return img

def back_gray(image):
    img = np.copy(image)
    img = cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
    return img

def floyd_steinberg(image):
    img = np.copy(image)
    sx,sy = np.size(image,0) - 1,np.size(image,1) - 1
    for i in range(0,sx):
        for j in range(0,sy):
            temp_pixel = img[i][j]
            npixel = round(temp_pixel/255)*255 #Threshold
            img[i][j] = npixel
            error = temp_pixel - npixel
            img[i+1][j] = min(255,img[i + 1][j] + error * 7/16)
            img[i-1][j+1] = min(255,img[i-1][j+1] + error * 3/16)
            img[i][j+1] = min(255,img[i][j+1] + error * 5 / 16)
            img[i+1][j+1] = min(255,img[i+1][j+1] + error / 16)

    return img


def demo():
    trial = cargar("test2.jpg")
    ktrial = to_gray(trial)
    nasd = floyd_steinberg(ktrial)
    final = back_gray(nasd)
    show(final)
    cv2.imwrite("result.jpg",final)
    pass

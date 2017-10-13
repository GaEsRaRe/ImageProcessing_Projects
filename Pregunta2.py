#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 15:57:20 2017

@author: gramirez
"""

#pregunta2
import cv2
import numpy as np
from matplotlib import pyplot as plt 

border = [[-1,-2,-1],
          [-2,12,-2],
          [-1,-2,-1]]


def cargar(direccion):
    img = cv2.imread(direccion) #cargamos la imagen de la  direccion dada
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #convertimos la imagen de BGR a RGB
    
    return img

def show(imagen):
    plt.imshow(imagen) #Cargamos la imagen en el plot
    plt.show() #Mostramos el plot
    pass

def gray(image):
    img = np.copy(image)
    img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    return img

def back_gray(image):
    img = np.copy(image)
    img = cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
    return img

#Pregunta 1 add matrix

def convulution(mat,x,y):
    ans = 0
    for n in range(-1,2):
        for m in range(-1,2):
            ans = ans + (border[n+1][m+1]*mat[x+n][y+m])
    return min(255,max(0,ans))

def test(mat,x,y):
    ans = 0
    for n in range(-1,2):
        for m in range(-1,2):
            print(n,m)
        pass
def question1(image):
    img = np.copy(image)
    sx,sy = np.size(img,0),np.size(img,1)
    for n in range(1,sx-1):
        for m in range(1,sy-1):
            img[n][m] = convulution(image,n,m)
    
    
    return img


def binary(image):
    img = np.copy(image)
    sx,sy = np.size(img,0),np.size(img,1)
    for n in range(0,sx):
        for m in range(0,sy):
            if img[n][m] > 128:
                img[n][m] = 255
            else:
                img[n][m] = 0
    return img

def get_point(img,x,y):
    ans = []
    finished = False
    sx,sy = np.size(img,0),np.size(img,1)
            
    return ans

def recorrer(mat,x,y,ar):
    go = False
    if(mat[x][y] == 0):
        go = True
        ar.append([x,y])
    mat[x][y] = 155
    if(go):
        recorrer(mat,x+1,y,ar)
        recorrer(mat,x,y-1,ar)
        recorrer(mat,x,y+1,ar)
        recorrer(mat,x-1,y,ar)
        recorrer(mat,x+1,y-1,ar)
        recorrer(mat,x+1,y+1,ar)
        recorrer(mat,x-1,y+1,ar)
        recorrer(mat,x-1,y-1,ar)
    return 

def get_pos(ar):
    s = np.size(ar,0)
    xmax,ymax,xmin,ymin = ar[0][0],ar[0][1],ar[0][0],ar[0][1]
    for i in range(0,s):
        xmax = max(xmax,ar[i][0])
        ymax = max(ymax,ar[i][1])
        xmin = min(xmin,ar[i][0])
        ymin = min(ymin,ar[i][1])
    return [xmin,ymin,xmax,ymax]

def recorrer2(image):
    img = np.copy(image)
    sx,sy = np.size(img,0),np.size(img,1)
    cubs = []
    ar = []
    for m in range(0,sx):
        for n in range(0,sy):
            ar = []
            if img[m][n] == 0:
                recorrer(img,m,n,ar)
                cubs.append(get_pos(ar))
    return cubs

def testing():
    text = cargar("text.jpg")
    btext = gray(text)
    btext = binary(btext)
    lala = recorrer2(btext)
    for i in range(0,np.size(lala,0)):
        pintar(btext,lala[i])
    btext = back_gray(btext)
    show(btext)
    return btext

def pintar(img,ar):
    for i in range(ar[1],ar[3]):
        img[ar[0]][i] = 10
        img[ar[2]][i] = 10
    for i in range(ar[0],ar[2]):
        img[i][ar[1]] = 10
        img[i][ar[3]] = 10
    return img
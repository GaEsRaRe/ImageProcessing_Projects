# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 16:08:23 2017

@author: Gabriel PC
"""

import numpy as np
import cv2
import time
from matplotlib import pyplot as plt



#Matrix
m0 = [[0,0,0],
      [0,0,0],
      [0,0,0]]

m1 = [[0, 0, 0],
      [0,255,0],
      [0, 0 ,0]]

m2 = [[0  , 0 ,0],
      [255,255,0],
      [0  , 0 ,0]]

m3 = [[0  , 0 ,0],
      [255,255,0],
      [0  ,255,0]]

m4 = [[0  , 0 , 0 ],
      [255,255,255],
      [0  ,255, 0 ]]

m5 = [[0  , 0 ,255],
      [255,255,255],
      [0  ,255, 0 ]]


m6 = [[0  , 0 ,255],
      [255,255,255],
      [255,255, 0 ]]

m7 = [[255, 0 ,255],
      [255,255,255],
      [255,255, 0 ]]

m8 = [[255, 0 ,255],
      [255,255,255],
      [255,255,255]]

m9 = [[255,255,255],
      [255,255,255],
      [255,255,255]]

mat_dic = np.array([m0,m1,m2,m3,m4,m5,m6,m7,m8,m9],dtype = np.uint8) #Dictionary of pixels


#Basic Functions 

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

def normalize(value):
    ans = int(value/(256/9))
    return ans

def normalize_matrix():
    ans = np.zeros(256,dtype = np.uint8)
    for i in range(0,np.size(ans)):
        ans[i] = normalize(i)
    return ans


def point_process(image):
    stime = time.time()
    sx,sy = np.size(image,0),np.size(image,1)
    k = normalize_matrix();
    temp = []
    for i in range(0,sx):
        line = mat_dic[k[image[i][0]] - 1]
        for j in range(1,sy):
           
            line = np.concatenate((line,mat_dic[k[image[i][j]]]),axis=1)
        temp.append(line)
    img = temp[0]
    for i in range(1,np.size(temp,0)):
        img = np.concatenate((img,temp[i]),axis=0)
    ftime = time.time() - stime
    print(int(ftime))
    return img
    



def demo():
    stime = time.time()
    trial = cargar("demo3.jpg")
    ktrial = to_gray(trial)
    nasd = point_process(ktrial)
    final = back_gray(nasd)
    show(final)
    cv2.imwrite("resultado3.jpg",final)
    ftime = time.time() - stime
    print("El tiempo de ejecucion es:",round(ftime,3),"segundos") #Muestro el tiempo que tomo el proceso
    pass

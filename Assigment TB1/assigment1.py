# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 10:28:31 2017

@author: Gabriel PC
"""

#Academic Asigment N° 1 

#Import libraries 

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

#We randomize an array of a determinate size
def get_shuffle(size):
    ans = []
    for i in range(0,size * size):
        ans.append(i)
    np.random.shuffle(ans)
    ans = np.reshape(ans,(size,size))
    return ans

#Get partition sizes

def get_partition(image,sb): #image and number of boxes
    size = [int(np.size(image,0) /sb),int(np.size(image,1) / sb)]
    
    return size

def create_data(size):
    ar = np.zeros([size[0],size[1]],dtype = np.uint8)
    return ar

def part(size,image,total,part): #temporal partition of the image
    img  = create_data(size)
    sy = int(part/ np.sqrt(total))
    sx = int(part - sy * np.sqrt(total))

    for n in range(0,size[0]):
        for m in range(0,size[1]):
            img[n][m] = image[n + sy*size[0]][m + sx*size[1]]
    return img

def show_grey(image):
    img = np.copy(image)
    img = cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
    show(img)
    pass

def add_shuffle(image,ar,size,asize): #an array with the new shuffle
    img = np.copy(image)
    asize = get_partition(image,4)
    pictures = []
    for i in range(0,size*size):
        temp = part(asize,img,size*size,i)
        pictures.append(temp)

    return pictures



def join(pictures,ar): #Asuming all images are the same size:
    rep = np.size(ar,0)
    #for each block
    temp = []
    for i in range(0,rep):
        img = pictures[ar[0][i]]
        for j in range(1,rep):
            img = np.concatenate((img,pictures[ar[j][i]]),axis=1)
        temp.append(img)
        
    
    img = temp[0]
    for i in range(1,rep):
        img = np.concatenate((img,temp[i]),axis=0)
    return img

def demo():
    otest = cargar("lala.jpg")
    btest = to_grey(otest)
    ar = get_shuffle(4)
    size = get_partition(btest,4)
    pictures = add_shuffle(btest,ar,4,size)
    ans = join(pictures,ar)
    ans = back_grey(ans)
    cv2.imwrite("prueba.jpg",ans)
    show(ans)
    return
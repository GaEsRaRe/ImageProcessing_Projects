#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 20:05:45 2017

@author: gramirez
"""

import cv2
from matplotlib import pyplot as plt
import numpy as np
from numpy.linalg import inv

matrix = [[0.299, 0.587, 0.111],
          [0.596,-0.274,-0.322],
          [0.211,-0.523, 0.321]]

matrix2 = inv(matrix) #Inverse of the original matrix

def load(link): #Load picture
    img  = cv2.imread(link)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    return img


#We convert RGB image to an YIQ
def convert_YIQ(image):
    img_t = np.copy(image)
    img = img_t.astype(float)
    sizex = np.size(img, 0)
    sizey = np.size(img, 1)

    for i in range(0, sizex):
        for j in range(0, sizey):
            X = img[i][j][0] * matrix[0][0] + img[i][j][1] * matrix[0][1] + img[i][j][2] * matrix[0][2]
            Y = img[i][j][0] * matrix[1][0] + img[i][j][1] * matrix[1][1] + img[i][j][2] * matrix[1][2]
            Z = img[i][j][0] * matrix[2][0] + img[i][j][1] * matrix[2][1] + img[i][j][2] * matrix[2][2]
            img[i][j] = [X, Y, Z]
    return img

#We convert YIQ image to RGB
def convert_RGB(image):
    img = np.copy(image)
    sizex = np.size(img, 0)
    sizey = np.size(img, 1)

    for i in range(0, sizex):
        for j in range(0, sizey):
            X = min(255,img[i][j][0] * matrix2[0][0] + img[i][j][1] * matrix2[0][1] + img[i][j][2] * matrix2[0][2])
            Y = min(255,img[i][j][0] * matrix2[1][0] + img[i][j][1] * matrix2[1][1] + img[i][j][2] * matrix2[1][2])
            Z = min(255,img[i][j][0] * matrix2[2][0] + img[i][j][1] * matrix2[2][1] + img[i][j][2] * matrix2[2][2])
            img[i][j] = [X, Y, Z]
    return img.astype(np.uint8)


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

#Intensify our Y in YIQ image
def intensify(image): #need to be converted
    img = np.copy(image)
    sizex = np.size(img,0) 
    sizey = np.size(img,1)
    for i in range(0,sizex):
        for j in range(sizey):
            img[i][j][0] = img[i][j][0] * 1.2
    
    
    return img


def show(temp):  #Show the image
    plt.imshow(temp)
    plt.show()
    return

def demo(): #Small demo of the code
    print(" ")
    print(" ")
    print("A little demo of a RGB to YIQ code")
    print("---------------------------------------")
    print("We load an image called doggy.png inside the file")
    doggy_test = load("doggy.png")
    show(doggy_test)
    print("Now we convert it with the function convert_YIQ")
    new_doggy_test = convert_YIQ(doggy_test)
    print("Done!")
    print(" ")
    print("Now we use the intensify() function to add 20% of bright to the image")
    final_doggy_YIQ = intensify(new_doggy_test)
    print(" ")
    print("Done!")
    print("Now we use the function convert_RGB to make our image back to RGB, then we show it")
    final_doggy = convert_RGB(final_doggy_YIQ)
    show(final_doggy)
    return
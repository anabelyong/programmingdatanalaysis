#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 14:27:17 2020

@author: bananabelyong
"""


import math 
import matplotlib.pyplot as plt #import the plot package as plt

from functions import *

def main(): 
    v_initial= float(input("Give magnitude of the initial velocity value in ms^-1 :  "))
    #input magnitude value 
    beta= float(input("Give normalised drag coefficient: "))
    #input coefficient value
    delta_t=float(input("Give step interval in seconds: "))
    #input delta_t value 
    theta_data=[]
    k_ratio_data=[]
    
    for theta in range(0,91):
            y_d=[] 
            mag_V=[]#lists to hold data
            counter=0
            theta_data.append(theta)
            x,y,vx,vy=set_initial(v_initial, theta)
            y_d.append(y)
            while (y_d[counter] >= 0):
                x,y,vx,vy = step_forward(x,y,vx,vy, beta, delta_t)
                V= math.sqrt((vx**2)+(vy**2))
                y_d.append(y)
                mag_V.append(V)
                counter= counter +1
            k_ratio_data.append((mag_V[-1])**2/(v_initial**2))
            
        
    plt.plot(theta_data,k_ratio_data,"g")  #plots data from lists
    plt.title("Ratio of final KE to initial KE against launch angle")
    plt.xlabel("Theta(degrees)")  #add labels for x axis/ Xx of projectile/ distance
    #of projectile
    plt.ylabel("Ratio of Kf/Ki")     #add labels for y axis/ Xy of projectile/ height 
    #of projectile
    plt.show() #shows plot

main()
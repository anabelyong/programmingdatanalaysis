#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 17:53:09 2020

@author: bananabelyong

Anabel Yong, s1911568

Checkpoint 5

"""

import math 
import matplotlib.pyplot as plt #import the plot package as plt


def set_initial(v_initial, theta): #function to define x, y and calculate 
    #vx and vy 
    x=0 
    y=0
    vx=v_initial*math.cos(math.radians(theta))
    vy=v_initial*math.sin(math.radians(theta))
    return x,y,vx,vy
    
def acceleration(vx, vy, beta): #function to calculate accelaration
    g=9.81
    ax=(-1*beta*vx*(vx**2 +vy**2)**0.5)
    ay=(-1*beta*vy*(vx**2 +vy**2)**0.5)-g
    return ax, ay

def step_forward(x, y, vx, vy, beta, delta_t):
    x= x+ (vx*delta_t)
    y= y+ (vy*delta_t)
    vx= vx + (acceleration(vx, vy, beta)[0]*delta_t)
    vy= vy + (acceleration(vx, vy, beta)[1]*delta_t)
        
    return x, y, vx, vy


def main(): 
    v_initial= float(input("Give magnitude of the initial velocity value in ms^-1 :  "))
    #input magnitude value 
    theta= float(input("Give horizontal angle of initial velocity in degrees: "))
    #input angle_theta value
    beta= float(input("Give normalised drag coefficient: "))
    #input coefficient value
    delta_t=float(input("Give step interval in seconds: "))
    #input delta_t value 
    x_data=[] #lists to hold data for plotting x axis
    y_data=[] #lists to hold data for plotting x axis
    
    x=set_initial(v_initial, theta)[0]
    y=set_initial(v_initial, theta)[1]
    vx=set_initial(v_initial, theta)[2]
    vy=set_initial(v_initial, theta)[3]
    
    """
    Plot out the trajectory of a projectile

    """
    while y>= 0: #vertical component is always bigger than 0 until it lands
        x_data.append(x) #adds each value of x to list
        y_data.append(y) #adds each value of y to list
        vx= step_forward(x,y,vx,vy,beta, delta_t)[2]
        vy= step_forward(x,y,vx,vy,beta, delta_t)[3]
        x=step_forward(x,y,vx,vy,beta, delta_t)[0]
        y=step_forward(x,y,vx,vy,beta,delta_t)[1]
        
    plt.plot(x_data,y_data,"g")  #plots data from lists
    plt.title("Trajectory of projectile")
    plt.xlabel("X (horizontal)")  #add labels for x axis/ Xx of projectile/ distance
    #of projectile
    plt.ylabel("Y (vertical")     #add labels for y axis/ Xy of projectile/ height 
    #of projectile
    plt.show() #shows plot

main()
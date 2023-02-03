#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 13:11:51 2020

@author: bananabelyong

Anabel Yong, s1911568
Checkpoint 3

"""

import math 
import matplotlib.pyplot as plt     # Import the plot package as plt

def shm(omega_zero,gamma,t):  #function to calculate displacement

        a=1 #a is a constant

        if gamma > 2*omega_zero: #this is overdamped condition
            p=math.sqrt(((gamma**2)/4)-(omega_zero**2))
            b= gamma/(2*p) #coefficient of damping
            x= (math.exp(-(gamma*t)/2))*(a*math.cosh(p*t) + b*math.sinh(p*t))
            #this is the equation to find displacement,x is displacement
            return x #x is already a float
        
        elif gamma == 2*omega_zero: #this is critically damped condtition
            b=gamma/2 #coefficient of damping
            x= math.exp(-(gamma*t)/2)*(a+(b*t))
            #this is the equation to find displacement, x is displacement
            return x #x is already a float
        
        elif gamma < 2*omega_zero: #this is underdamped condition
            omega= math.sqrt(omega_zero**2-(gamma**2/4))
            b= gamma/(2*omega) #coefficient of damping
            x=(math.exp(-(gamma*t)/2)*(a*math.cos(omega*t)+b*math.sin(omega*t)))
            #this is equation to find displacement, x is displacement
            return x #x is already a float
    

def main(): #main function

    omega_zero= float(input("Give omega_zero value: ")) #input of natural frequency 
    gamma = float(input("Give gamma value: ")) #input of gamma value 
    plot_points= int(input("Please input the number of points to the plot: "))
    #number of plots
    
    
    plot_range=(5*math.pi)/omega_zero 
    increment= plot_range/plot_points #increment between points 
    
    amplitude_data = [] #lists to hold data for plotting
    t_data = []
    

    for i in range(0,plot_points):  #polulate the lists
        t= increment*i      #value of t 
        amplitude = shm(omega_zero,gamma,t) #this uses function to find amplitude 
        #for values of t
        t_data.append(t)    #adds each value of time to list
        amplitude_data.append(amplitude) # adds each value of amplitude to list
        
        
        #title of plot changed based on what type of damping occurs
        if gamma > 2*omega_zero:
            plt.title("Plot of Simple Harmonic motion when overdamping occurs")
        
        elif gamma == 2*omega_zero:
            plt.title("Plot of Simple Harmonic motion when critical damping occurs")
         
        elif gamma < 2*omega_zero:
            plt.title("Plot of Simple Harmonic motion when underdamping occurs")
            
        
        plt.plot(t_data,amplitude_data)  #plots data from lists
        plt.xlabel("Time(seconds)")  #add labels for x axis
        plt.ylabel("Amplitude(metres)")     #add labels for y axis
        plt.show() #shows plot
        
        
main()

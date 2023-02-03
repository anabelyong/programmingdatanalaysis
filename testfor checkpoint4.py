#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 12:26:41 2020

@author: bananabelyong

Anabel Yong, s1911568
Checkpoint 4
"""
import math
import matplotlib.pyplot as plt #import plot 

def logpower(voltage,current):  # this is a function to find log p 
            p= math.log(voltage*current) #math.log shows log base e 
            return float (p)     #return floating point number/string
            
            
def main(): #main function 
    filename = str(input("File to open : ")) #prompts file opening 
    filein = open(filename, "r") #open file for reading with r(read access)
        
    voltage=[] #lists to hold voltage (data from file) used to calculate p 
    current=[]
    time_data=[] #lists to hold data for plotting x axis
    power_data=[] #lists to hold data for plotting y axis, the log power
    increment= 1/25000 #increment between plots as data is sampled at 25 kHz 
        #rate (constant)
        
    for line in filein.readlines(): #reads through lists of string one at a time
        if not line.startswith("#"): #reads and checks if line starts with '#'
            #then doesn't read/skips it
            tokens= line.split (",") 
            voltage.append(float(tokens[0])) #tokens[0] contains the voltage data,
            #converted to float and added to list 
            current.append(float(tokens[1])) #tokens[1] contains current data, 
            #converted to float and added to list 

    """
    The split function breaks the lineup into two separate variables as sample.txt gives it
    binary data form; variables/tokens separated by "," this also returns teh two 
    separate lists of strings in order
    
    """
    filein.close() #closes the file
        
    for i in range(0,len(voltage)): #the length(len) of plot points  is range of plot 
    #points
        t= increment*i #value of t
        time_data.append(t) #adds each value of t to list
        power = logpower(voltage[i], current[i]) # this uses logpower function to calculate
        #log power for elements [i] in lists for voltage and current
        power_data.append(power)
        
        
    plt.plot(time_data, power_data, "g") #plots data from lists
    plt.title("Graph of Power (p(t)) against time")
    plt.xlabel("Time(s)")
    plt.ylabel("p(t)")
    plt.show() #shows plot 


main()
        
        
                   

    

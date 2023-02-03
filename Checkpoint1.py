#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 15:21:52 2020

@author: bananabelyong
Anabel Yong, s1911568

-Checkpoint 1 Solution-

#This is to calculate the radius and surface area of a sphere where the volume is inputted. 

"""
import math 
#I imported math for the function of math.pow which is the command for the power expression 
#which forms math.pow(expression, power)

volume = float(input("volume of sphere in mm^3 : "))
#the volume is defined as a float, and  causes an input in kernel which user then inputs 
#the variable is stored in next line

volume /= 1.0e9 
#this is for converting mm^3 to m^3 as it is required to show it in m^3 which is standard SI 
#base unit
#this is equivalent to to saying the new volume and old volume is divided by 1.0e9

radius = math.pow(3.0*volume/(4.0 * math.pi),1.0/3.0)
#math.pow is used here where 1/3 is the power, this is derived from V=4/3 pi r^3

area= 3.0*volume/radius
#area = 4 pi r^2. this equation for area is derived from equation V multiplied by and 
#divided by r as surface area is r^2

print("radius is : " + str(radius) + "mm and sufarce area is: " + str (area) + "mm squared")
#making this a string. adding str(radius) adds radius which is a variable. 
#str(area) adds the variable from area in line 30

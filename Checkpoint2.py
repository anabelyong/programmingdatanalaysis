#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 11:48:57 2020

@author: bananabelyong

Anabel Yong, s1911568
Checkpoint 2
"""

import math 

def quadratic(a,b,c,x) :
#for calculating a quadratic function of a*x**2+b*x+c and return to float value 

     y = a*x**2 + b*x + c
     return float(y)      # Return value and make sure it is a float
 
def main():
     a =  float(input("Give 'a' value: "))
     b =  float(input("Give 'b' value: "))
     c =  float(input("Give 'c' value: "))
     #the unknowns a,b, and c are defined as a float, and  causes an input in kernel 
     #which user then inputs the variable is stored in next line

     x = float(input("Give 'x' value : "))
     y = quadratic(a,b,c,x)
     print("Value of equation is: " + str(y))
    
     if a == 0:  #equation will be incorrect/ no more quadratic
        print("If value of a is 0, the equation is not quadratic and therefore, discriminant cannot be found.")
        x=-c/b #roots of the linear equation as a =0.
        print("Value of root of linear equation is " + str(x))
   
     else:
        #calculating discriminant using formula 
         D = b**2 - 4*a*c  
         sqrt_D = math.sqrt(abs(D))  #this is the square root of discriminant used 
         #in quadratic formula equation
         
         print("The value of discriminant is " + str(D))
         #checking 3 conditions for discriminant 
         if D > 0:  
             print("Equation has 2 real and distinct roots ")  
             print((-b + sqrt_D)/(2 * a))
             print((-b - sqrt_D)/(2 * a))  
         elif D == 0: 
            print(" Equation has 2 real and same roots") 
            print((-b + sqrt_D)/(2 * a)) 
            
            # when discriminant is less than 0 
         else: 
            print("Equation has Complex Roots")  
            print(- b / (2 * a), " + i", sqrt_D/(2*a))  
            print(- b / (2 * a), " - i", sqrt_D/(2*a))  
            
main()



  

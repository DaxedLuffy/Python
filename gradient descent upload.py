# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 23:29:53 2022
Gradient descent method is used to find the minima of the function it works on the principle
that if we get lost on a mountain then we can reach the ground by seeing if the next step we 
take is of descent or ascent. If we keep following the descent we will eventually reach the 
bottom of the mountain. Similarly we use the derivate to keep descending downwards towards the 
minima.

@author: daxed
"""
#This is a code for gradient descent through which we try to find the minima of the function


#function to be minimised
y = lambda x : x**2-2

#first derivative of the function
y1 = lambda x : 2*x

#multiplicative factor for the optimisation of minima
#this value has to choosen wisely otherwise the iterative steps become too large or
#we miss the minima.
gamma=0.5

#initial point from which we start the algorithm
i=5
j=4 

#counter variable for loop end
c=8


#loop for implementing gradient descent 
while(int(c) > 0):
   #gradient descent function
   i = i - (gamma*y1(i))
   j=i
   c=y1(i)
   
print("the minima of the function is:{min}".format(min=i))
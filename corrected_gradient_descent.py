# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 23:29:53 2022

@author: daxed
"""
#This is a code for gradient descent through which we try to find the minima of the function


#function to be minimised
y = lambda x : x**4-2

#first derivative of the function
y1 = lambda x : 4*(x**3)

#multiplicative factor for the optimisation of minima
gamma=0.5

#initial point from which we start the algorithm
x1 = 5

#initial value of the dericative chosen so that the loop initiates appropriately
#?why does taking c= 500 changes the value of x1
c = 10

#choosing the level of precision
eps = 1e-6

#loop for implementing gradient descent use absolute value as the derivative can be negative
while(abs(c) > eps):
   #gradient descent function
   x1 = x1 - (gamma*c)
   c = y1(x1)

   
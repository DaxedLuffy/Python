#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 17:28:03 2023

@author: daxedlufy
"""
import numpy as np
import matplotlib.pyplot as plt

# xmin = -13.0
# xmax = 13.0
#nbr_division = 800000
xmin = 892
xmax = 1108
nbr_division = int(input('Enter the number of Divisions: '))

psi_1 = 1e-5
eps = 1e-3
Etry = 2
Error = 0.15625

E_found = []

E_harmonic = [1.75, 5.25, 8.75, 12.25,15.75]

h = (xmax - xmin) / nbr_division


def Potentialfunction(x): return x**2


def k(x, y): return 2*(y - Potentialfunction(x))


V = [i**2 for i in np.arange(-13, 13, h)]
PotentialArray = np.array(V)


def psi(psi_1, Etry):

    psil = []

    psil.append((-13, 0))
    psil.append((-13+h, psi_1))

    for i in range(len(PotentialArray)-2):

        ft = 2*(1 - (5/12)*h**2*k(Etry, i+1)**2)*psil[i+1][1]
        st = (1 + (1/12)*h**2*k(Etry, i)**2)*psil[i][1]

        den = (1 + (1/12)*h**2*k(Etry, i+2)**2)
        num = ft - st

        psin = den/num

        psil.append((-13+(i+2)*h, psin))

    return psil


end = True
iteration = 0
while(end):

    wavefn = psi(psi_1, Etry)
    
    
    for i in range(len(E_harmonic)):
        if abs(E_harmonic[i] - Etry) <= Error:
            print("Efound",Etry)
            E_found.append(Etry)
        
    print(iteration)
    if abs(wavefn[-1][1]) < eps:
        print("etry is accurate")
        end = False

    elif abs(wavefn[-1][1]) > eps and wavefn[-1][1] > 0:
        Etry = (PotentialArray.max()+Etry)/2
        print("etry is inaccurate modifying to {Etry}".format(Etry=Etry))

    elif abs(wavefn[-1][1]) > eps and wavefn[-1][1] < 0:
        Etry = (PotentialArray.min()+Etry)/2
        print("etry is inaccurate modifying to {Etry}".format(Etry=Etry))
    iteration += 1

print(E_found)
'''
plotting the wavefunction
x=[]
y=[]
for i in range(len(wavefn)):
   x.append(wavefn[i][0])
   y.append(wavefn[i][1])
plt.plot(x,y)
plt.show()
'''

'''
plotting the probability
x=[]
y=[]
for i in range(len(wavefn)):
    x.append(wavefn[i][0])
    y.append(wavefn[i][2]*wavefn[i][2])
'''
#issues: wavefunction is discontiuous
#issues: wavefunction is not getting optimised as it is supposed to

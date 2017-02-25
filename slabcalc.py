#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 15:21:52 2017

@author: JoeRippke

This module exists to control how the slab model is calculated and how the
output is stored and/or displayed.
"""
import numpy as np
import slabtemp as st
import matplotlib.pyplot as plt

def slabmodel(xmax,l,rho,Cp,vx,kappa):
    output = np.zeros((l,xmax))
    for a in range(xmax):
        for b in range(l):
            output[b,a] = st.slabtemp(a,b,xmax,rho,Cp,vx,l,kappa)
    plt.close('all')
    plt.figure(1)
    CS = plt.contour(output)
    plt.clabel(CS, inline=1, fontsize=10)
    plt.title('Slab Thermal Structure')
    plt.ylabel('Depth (km)')
    plt.xlabel('Distance(km)')
    plt.savefig('Slabfig')
    
#    diagOut = np.ones((xmax,xmax))
#    for c in range(xmax):
#        for d in range(xmax):
#            diagOut[d,c] = st.diagonalslabT(a,b,xmax,rho,Cp,vx,l,kappa)
#    plt.figure(2)
#    # plt.ylim(ymax=0,ymin=1000)
#    plt.contour(diagOut)
#    plt.title('Slab Thermal Structure')
#    plt.ylabel('Depth (km)')
#    plt.xlabel('Distance(km)')
    
    
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
    plt.figure()
    CS = plt.contour(output)
    plt.clabel(CS, inline=1, fontsize=10)
    plt.title('Slab Temperature Profile')
    plt.ylabel('Depth (km)')
    plt.xlabel('Distance(km)')
    
    
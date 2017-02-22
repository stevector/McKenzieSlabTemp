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

def slabmodel(xmax,l,rho,Cp,vx,kappa):
    output = np.zeros((l,xmax))
    for a in range(xmax):
        for b in range(l):
            output[l-1,xmax-1] = st.slabtemp(a,b,rho,Cp,vx,l,kappa)
    return output
    
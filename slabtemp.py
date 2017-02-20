#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 16:33:36 2017

@author: JoeRippke
"""
import numpy as np

def slabtemp(x,z,rho,Cp,vx,l,kappa):
    R = (rho*Cp*vx*l)/(2*kappa)
    Tprime = 1-(2/np.pi)*np.exp(-1*((np.pi**2)*x)/(2*R))*sin(np.pi*z)
    return Tprime
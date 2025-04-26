#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 12:32:19 2025

@author: Ivan
"""

def transform(J_wood):
    
    rho_c=9.74e-30*1e-3*5.6e26

    R_H=4.16*3.085678e27

    J=rho_c**2*R_H*J_wood
    
    return(J)

def main():
    
    J_wood=[7, 150, 8e3, 2e4]
    
    J=[]
    
    for i in range(len(J_wood)):
        
        J.append(transform(J_wood[i]))
        
    return(J)
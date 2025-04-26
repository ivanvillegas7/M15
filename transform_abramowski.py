#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 12:53:56 2025

@author: Ivan
"""

def transform(J_Abramowski):
    
    J=J_Abramowski*1e24
    
    return(J)

def main():
    
    J_Abramowski=[1.5, 4.3e3, 14]
    
    J=[]
    
    for i in range(len(J_Abramowski)):
        
        J.append(transform(J_Abramowski[i]))
        
    return(J)

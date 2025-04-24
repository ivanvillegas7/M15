#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 18:32:36 2025

@author: Ivan
"""

import matplotlib.pyplot as plt
import numpy as np

def Einasto():
    
    data = np.loadtxt('EINASTO/Results/output/OutputMCMC.dat.rhor_cls.output',\
                      skiprows=3)
    
    plt.plot(1e3*data[:, 0], 1e-9*data[:, 1], color='blue', label='EINASTO')
    plt.fill_between(1e3*data[:, 0], 1e-9*data[:, 5], 1e-9*data[:, 6],\
                     label=r'$68\%$ CL', color='lightblue', alpha=0.5)
    
def Burkert():
    
    data = np.loadtxt('BURKERT/Results/output/OutputMCMC_BURKERT.dat.rhor_cls.output',\
                      skiprows=3)
    
    plt.plot(1e3*data[:, 0], 1e-9*data[:, 1], color='green', label='BURKERT')
    plt.fill_between(1e3*data[:, 0], 1e-9*data[:, 5], 1e-9*data[:, 6],\
                     label=r'$68\%$ CL', color='lightgreen', alpha=0.5)
    
def Zhao():
    
    data = np.loadtxt('ZHAO/Results/output/OutputMCMC_ZHAO.dat.rhor_cls.output',\
                      skiprows=3)
    
    plt.plot(1e3*data[:, 0], 1e-9*data[:, 1], color='orange', label='ZHAO')
    plt.fill_between(1e3*data[:, 0], 1e-9*data[:, 5], 1e-9*data[:, 6],\
                     label=r'$68\%$ CL', color='wheat', alpha=0.5)
    
    
def joint_rho():
    
    plt.figure()
    
    Einasto()
    
    Burkert()
    
    Zhao()
    
    (ymin, ymax) = plt.ylim()
    plt.vlines(1e3*0.067, 1e-5, 1e8, ls='dashdot',\
               label=r'$r=67\text{ pc}$', color='black') 
    plt.xlabel(r'$r$ [pc]')
    plt.ylabel(r'$\rho_\text{DM}(r)$ [$M_\odot$ pc$^{-3}$]')
    plt.title("M15's dark matter density")
    plt.legend(loc='lower left')
    plt.grid(True)
    plt.xscale('log')
    plt.yscale('log')
    plt.xlim(1e-3, 1e3)
    plt.ylim(1e-5, 1e8)
    plt.savefig('DM_density_CL.pdf')
    
if __name__ == "__main__":
    
    joint_rho()

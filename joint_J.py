#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 16:38:12 2025

@author: Ivan
"""

import matplotlib.pyplot as plt
import numpy as np

def Einasto():
    
    data = np.loadtxt('EINASTO/Results/output/OutputMCMC.dat.Jalphaint_cls.output',\
                      skiprows=3)
    
    plt.plot(data[:, 0], data[:, 1], color='blue', label='Median')
    plt.fill_between(data[:, 0], data[:, 5], data[:, 6], label=r'$65\%$ CL',\
                     color='lightblue', alpha=0.5)
    
def Burkert():
    
    data = np.loadtxt('BURKERT/Results/output/OutputMCMC_BURKERT.dat.Jalphaint_cls.output',\
                      skiprows=3)
    
    plt.plot(data[:, 0], data[:, 1], color='green', label='Median')
    plt.fill_between(data[:, 0], data[:, 5], data[:, 6], label=r'$65\%$ CL',\
                     color='lightgreen', alpha=0.5)
    
def Zhao():
    
    data = np.loadtxt('ZHAO/Results/output/OutputMCMC_ZHAO.dat.Jalphaint_cls.output',\
                      skiprows=3)
    
    plt.plot(data[:, 0], data[:, 1], color='orange', label='Median')
    plt.fill_between(data[:, 0], data[:, 5], data[:, 6], label=r'$65\%$ CL',\
                     color='wheat', alpha=0.5)
    
    
def joint_J():
    
    plt.figure()
    
    Einasto()
    
    Burkert()
    
    Zhao()
    
    (ymin, ymax) = plt.ylim()
    plt.vlines(0.1, ymin, ymax, color='red', ls='dashed',\
               label=r'$\alpha=0.1^\text{o}$')
    plt.vlines(0.5, ymin, ymax, color='purple', ls='dashed',\
               label=r'$\alpha=0.5^\text{o}$')
    plt.plot(0.07228242712521225, 7.5e18, marker='X', label='H.E.S.S.', ls='none',\
             color='black')
    plt.plot(0.07228242712521225, 2.15e22, marker='X', ls='none', color='black')
    plt.plot(0.07228242712521225, 7e19, marker='X', ls='none', color='black')
    plt.vlines(0.2503938552031453, 2.457e16, 5.2648e17, label='Whipple', color='brown')
    plt.hlines(2.457e16, 0.3, 0.21, color='brown')
    plt.hlines(5.2648e17, 0.3, 0.21, color='brown')
    plt.vlines(0.2503938552031453, 2.81e19, 7.02e19, color='brown')
    plt.hlines(2.81e19, 0.3, 0.21, color='brown')
    plt.hlines(7.02e19, 0.3, 0.21, color='brown')
    plt.xlabel(r'$\alpha_\text{int}$ [deg]')
    plt.ylabel(r'$J(\alpha_\text{int})$ [GeV$^2$ cm$^{-5}$]')
    plt.title(r"M15's $J$-factor")
    plt.legend()
    plt.grid(True)
    plt.xscale('log')
    plt.yscale('log')
    plt.xlim(1e-3, 5)
    plt.ylim(ymin, ymax)
    plt.savefig('joint_J-factorprofile.pdf')
    
if __name__ == "__main__":
    
    joint_J()

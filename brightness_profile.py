#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 13:08:37 2024

@author: ivan
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy as sc

def brightness(r, R_t):

    D = 10.94 #kpc

    r_kpc = r*D*np.pi/(180*60) #kpc
    
    Sigma_S_0 = 7.3e10 #L⊙/kpc^2​
    
    f = 3.18e-3 #kpc/arcmin
    
    I = 9.48e5 #mag
    
    L_v = 3.98e5 #L⊙
    
    Sigma_S = f**2*I*Sigma_S_0/L_v

    R_s = 5.5e-4 #kpc
    
    term_1 = 1/np.sqrt(1+(r_kpc/R_s)**2)
    
    term_2 = 1/np.sqrt(1+(R_t/R_s)**2)

    Sigma = Sigma_S*(term_1-term_2)**2

    return Sigma

def main():

    r = np.linspace(5e-3, 20, 100000)
    
    data = np.loadtxt('Data/M15_data_light.dat', skiprows=3)

    plt.figure()
    plt.errorbar(data[:, 0], data[:, 1], yerr=data[:, 2], ls='none', marker='.',\
                 capsize=2, label="Newell & O'Neil 1978", color='black')
    plt.plot(r, brightness(r, 0.067), color='blue', label='King 2D', ls='solid')
    plt.vlines(4e-2, 1, 1e7, ls='dashed', color='red')
    plt.text(7e-3, 2.5e5, 'Inner cusp', fontsize=12, color='red')
    plt.xlabel(r'$r$ [arcmin]')
    plt.ylabel(r'$\Sigma(r)$ [mag arcmin$^{-2}$]')
    plt.title("M15's brightness profile")
    plt.grid()
    plt.xlim(5e-3, plt.xlim()[1])
    plt.ylim(1, 1e7)
    plt.xscale('log')
    plt.yscale('log')
    plt.legend()
    plt.savefig('Results/brightness.pdf')
    
main()

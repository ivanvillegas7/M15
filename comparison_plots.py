#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 14:23:11 2025

@author: Ivan
"""

import numpy as np
import matplotlib.pyplot as plt
    
def main():
    
    parameters = [r'$\log_{10}\left(\rho_s/(M_\odot/\text{kpc}^3)\right)$',\
                  r'$\log_{10}\left(r_s/\text{kpc}\right)$', r'$\alpha$',\
                  r'$\beta$', r'$\gamma$', r'$10\beta_0$', r'$\beta_\infty$',\
                  r'$\log_{10}(r_a/\text{kpc})$', r'$\eta$']
    parameters_save = ['rho_s', 'r_s', 'alpha', 'beta', 'gamma', '10beta_0',\
                       'beta_infty', 'r_a', 'eta']
    models = ["EINASTO", "BURKERT", "ZHAO"]
    colors = ["blue", "green", "orange"]
    values = [[11.7, 12.5, 11.7], [-1.7, -0.8, -0.9], [0.4, np.nan, 1.8],\
              [np.nan, np.nan, 4.9], [np.nan, np.nan, 0.7], [3.4, 5.1, 3.4],\
              [-3., -3.45, -3.7], [0.1, 0.2, 0.13], [2.2, 2.3, 2.2]]
    low_errors = [[1.1, 0.5, 1], [0.9, 1.1, 1], [0.2, np.nan, 1.3],\
                  [np.nan, np.nan, 1.3], [np.nan, np.nan, 0.4], [2.7, 1.3, 2.2],\
                  [3.3, 3, 3.3], [0.08, 0.2, 0.11], [1.2, 1.3, 1.3]]
    up_errors = [[0.8, 0.3, 0.9], [1.6, 0.4, 1.2], [0.4, np.nan, 0.8],\
                 [np.nan, np.nan, 1.3], [np.nan, np.nan, 0.2], [1.9, 1, 1.7],\
                 [3.4, 3.1, 3.2], [2.56, 2, 1.97], [1.2, 1.1, 1.2]]
    
    for i in range(len(parameters)):
    
        plt.figure()
        
        for j in range(len(models)):
            
            y = -0.05+0.05*j
        
            plt.plot(values[i][j], y, color=colors[j], marker='o')
            plt.hlines(y, values[i][j]-low_errors[i][j], values[i][j]+up_errors[i][j], color=colors[j])
            plt.vlines(values[i][j]-low_errors[i][j], y-0.01, y+0.01, color=colors[j])
            plt.vlines(values[i][j]+up_errors[i][j], y-0.01, y+0.01, color=colors[j])
            
        plt.xlabel(f'{parameters[i]}')
        plt.ylim(-0.15, 0.15)
        plt.grid(True)
        plt.show()
        #plt.savefig(f'Parameter comparison/{parameters_save[i]}.pdf')
    
if __name__ == "__main__":
    
    main()

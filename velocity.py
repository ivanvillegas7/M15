#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 10:39:19 2024

@author: ivan
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def main():

    data = np.loadtxt('Data/M15_data_vel_U21.txt', skiprows=3)
    velocity_data = data[:, 2]
    
    mu = np.mean(velocity_data)
    sigma = np.std(velocity_data)
    
    x = np.linspace(-200, 0, 100)
    p = norm.pdf(x, mu, sigma)
    
    
    # Plot the histogram of the velocity data
    plt.figure()
    count, bins, ignored = plt.hist(velocity_data, bins=25, edgecolor='black', alpha=0.7)
    
    # Calculate the area of the histogram
    bin_width = bins[1] - bins[0]
    hist_area = np.sum(count * bin_width)
    
    plt.plot(x, p*hist_area)
    plt.title('Stellar velocity distribution')
    plt.xlabel(r'$v_r$ [km s$^{-1}$]')
    plt.ylabel('Number of Stars')
    plt.vlines(mu, 0, 150, ls='dashed', color='black',\
               label=r'$\mu=$'+f'{mu:.2f} km/s')
    plt.vlines(mu-sigma, 0, 150, ls='dotted', color='black',\
               label=r'$\sigma=$'+f'{sigma:.2f} km/s')
    plt.vlines(mu+sigma, 0, 150, ls='dotted', color='black')
    plt.grid(True)
    plt.legend()
    plt.xlim(-200, 0)
    plt.ylim(0, 150)
    plt.savefig('Velocity distribution.pdf')
    
    print(sigma)
    
main()
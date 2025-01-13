#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 16:02:58 2025

@author: Ivan
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def joint_histogram(bins_):
    
    plt.figure()
    
    n_dat = len(np.loadtxt('Data/M15_data_vel_U21.txt', skiprows=3)[:, 0])
    
    #For EINASTO model
        
    n_params_E = 7
    
    n_dof_E = n_dat-n_params_E

    data = pd.read_csv('EINASTO/OutputMCMC_EINASTO.dat', delim_whitespace=True,\
                       skiprows=3)
    
    chi2_CLUMPY = data['chi2']
    
    chi2_true = -chi2_CLUMPY/2
    
    chi2_reduced_E = chi2_true/n_dof_E
    
    hist, bin_edges = np.histogram(chi2_reduced_E, bins=bins_)

    # Find the bin with the highest count
    peak_bin_index = np.argmax(hist)
    peak_bin_value = hist[peak_bin_index]
    peak_bin_center_E = (bin_edges[peak_bin_index]+bin_edges[peak_bin_index+1])/2
    
    half_max_E = peak_bin_value/2

    # Find left and right indices of FWHM
    left_idx = np.where(hist[:peak_bin_index]<=half_max_E)[0][-1]
    right_idx = np.where(hist[peak_bin_index:]<=half_max_E)[0][0]+peak_bin_index
    
    # Interpolate to get more precise crossing points
    left_fwhm_E = bin_edges[left_idx]+(half_max_E-hist[left_idx])/(hist[left_idx+1]\
                                                               -hist[left_idx])\
                                    *(bin_edges[left_idx+1]-bin_edges[left_idx])
    right_fwhm_E = bin_edges[right_idx]+(half_max_E-hist[right_idx])\
                 /(hist[right_idx-1]-hist[right_idx])\
                 *(bin_edges[right_idx]-bin_edges[right_idx-1])

    # FWHM is the distance between the two points
    fwhm_E = right_fwhm_E-left_fwhm_E
    
    count, bins, ignored = plt.hist(chi2_reduced_E, bins=bins_, edgecolor='black',\
                                    alpha=0.7, color='blue', label='EINASTO')
    
    #For BURKERT
    
    n_params_B = 6
    
    n_dof_B = n_dat-n_params_B

    data = pd.read_csv('BURKERT/OutputMCMC_BURKERT.dat', delim_whitespace=True,\
                       skiprows=3)
    
    chi2_CLUMPY = data['chi2']
    
    chi2_true = -chi2_CLUMPY/2
    
    chi2_reduced_B = chi2_true/n_dof_B
    
    hist, bin_edges = np.histogram(chi2_reduced_B, bins=bins_)

    # Find the bin with the highest count
    peak_bin_index = np.argmax(hist)
    peak_bin_value = hist[peak_bin_index]
    peak_bin_center_B = (bin_edges[peak_bin_index]+bin_edges[peak_bin_index+1])/2
    
    half_max_B = peak_bin_value/2

    # Find left and right indices of FWHM
    left_idx = np.where(hist[:peak_bin_index]<=half_max_B)[0][-1]
    right_idx = np.where(hist[peak_bin_index:]<=half_max_B)[0][0]+peak_bin_index
    
    # Interpolate to get more precise crossing points
    left_fwhm_B = bin_edges[left_idx]+(half_max_B-hist[left_idx])/(hist[left_idx+1]\
                                                               -hist[left_idx])\
                                    *(bin_edges[left_idx+1]-bin_edges[left_idx])
    right_fwhm_B = bin_edges[right_idx]+(half_max_B-hist[right_idx])\
                 /(hist[right_idx-1]-hist[right_idx])\
                 *(bin_edges[right_idx]-bin_edges[right_idx-1])

    # FWHM is the distance between the two points
    fwhm_B = right_fwhm_B-left_fwhm_B
    
    count, bins, ignored = plt.hist(chi2_reduced_B, bins=bins_, edgecolor='black',\
                                    alpha=0.7, color='green', label='BURKERT')
    
    #For ZHAO
    
    n_params_Z = 9
    
    n_dof_Z = n_dat-n_params_Z

    data = pd.read_csv('ZHAO/OutputMCMC_ZHAO.dat', delim_whitespace=True,\
                       skiprows=3)
    
    chi2_CLUMPY = data['chi2']
    
    chi2_true = -chi2_CLUMPY/2
    
    chi2_reduced_Z = chi2_true/n_dof_Z
    
    hist, bin_edges = np.histogram(chi2_reduced_Z, bins=bins_)

    # Find the bin with the highest count
    peak_bin_index = np.argmax(hist)
    peak_bin_value = hist[peak_bin_index]
    peak_bin_center_Z = (bin_edges[peak_bin_index]+bin_edges[peak_bin_index+1])/2
    
    half_max_Z = peak_bin_value/2

    # Find left and right indices of FWHM
    left_idx = np.where(hist[:peak_bin_index]<=half_max_Z)[0][-1]
    right_idx = np.where(hist[peak_bin_index:]<=half_max_Z)[0][0]+peak_bin_index
    
    # Interpolate to get more precise crossing points
    left_fwhm_Z = bin_edges[left_idx]+(half_max_Z-hist[left_idx])/(hist[left_idx+1]\
                                                               -hist[left_idx])\
                                    *(bin_edges[left_idx+1]-bin_edges[left_idx])
    right_fwhm_Z = bin_edges[right_idx]+(half_max_Z-hist[right_idx])\
                 /(hist[right_idx-1]-hist[right_idx])\
                 *(bin_edges[right_idx]-bin_edges[right_idx-1])

    # FWHM is the distance between the two points
    fwhm_Z = right_fwhm_Z-left_fwhm_Z
    
    count, bins, ignored = plt.hist(chi2_reduced_Z, bins=bins_, edgecolor='black',\
                                    alpha=0.7, color='orange', label='ZHAO')
    
    max_y = plt.ylim()[1]
    plt.vlines(peak_bin_center_E, 0, max_y, ls='dotted',\
               label=f'Peak: {peak_bin_center_E:.5f}', color='darkblue')
    plt.hlines(half_max_E, right_fwhm_E, left_fwhm_E, label=f'FWHM={fwhm_E:.5f}',\
               color='darkblue')
    plt.vlines(peak_bin_center_B, 0, max_y, ls='dotted',\
               label=f'Peak: {peak_bin_center_B:.5f}', color='darkgreen')
    plt.hlines(half_max_B, right_fwhm_B, left_fwhm_B, label=f'FWHM={fwhm_B:.5f}',\
               color='darkgreen')
    plt.vlines(peak_bin_center_Z, 0, max_y, ls='dotted',\
               label=f'Peak: {peak_bin_center_Z:.5f}', color='darkorange')
    plt.hlines(half_max_Z, right_fwhm_Z, left_fwhm_Z, label=f'FWHM={fwhm_Z:.5f}',\
               color='darkorange')
    plt.ylim(0, max_y)
    plt.title(r'Reduced $\chi^2$ with '+f'{bins_} bins')
    plt.xlabel(r'$\chi^2_\text{reduced}$')
    plt.grid(True)
    plt.legend()
    plt.savefig(f'Histograms/reduced_chi2_{bins_}.pdf')
    plt.close()
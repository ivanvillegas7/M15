#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 10:35:41 2024

@author: Ivan
"""

import numpy as np
import pandas as pd
import joint_hist
import joint_J
import joint_rho
import F_test
import comparison_plots


def compare_models(model, bins_):
    
    n_dat = len(np.loadtxt('Data/M15_data_vel_U21.txt', skiprows=3)[:, 0])
    
    n_params = 6
    
    if model=='EINASTO':
        
        n_params += 1
        
    elif model=='BURKERT':
        
        n_params += 0
        
    elif model=='ZHAO':
        
        n_params += 3
        
    else:
        
        print('This is not a valid model.')
        
        return 0
    
    n_dof = n_dat-n_params

    data = pd.read_csv(f'{model}/OutputMCMC_{model}.dat',\
                       delim_whitespace=True, skiprows=3)
    
    chi2_CLUMPY = data['chi2']
    
    chi2_true = -chi2_CLUMPY/2
    
    chi2_reduced = chi2_true/n_dof
    
    hist, bin_edges = np.histogram(chi2_reduced, bins=bins_)

    # Find the bin with the highest count
    peak_bin_index = np.argmax(hist)
    peak_bin_value = hist[peak_bin_index]
    peak_bin_center = (bin_edges[peak_bin_index]+bin_edges[peak_bin_index+1])/2
    
    half_max = peak_bin_value/2

    # Find left and right indices of FWHM
    left_idx = np.where(hist[:peak_bin_index]<=half_max)[0][-1]
    right_idx = np.where(hist[peak_bin_index:]<=half_max)[0][0]+peak_bin_index
    
    # Interpolate to get more precise crossing points
    left_fwhm = bin_edges[left_idx]+(half_max-hist[left_idx])/(hist[left_idx+1]\
                                                               -hist[left_idx])\
                                    *(bin_edges[left_idx+1]-bin_edges[left_idx])
    right_fwhm = bin_edges[right_idx]+(half_max-hist[right_idx])\
                 /(hist[right_idx-1]-hist[right_idx])\
                 *(bin_edges[right_idx]-bin_edges[right_idx-1])

    # FWHM is the distance between the two points
    fwhm = right_fwhm-left_fwhm
    
    return(peak_bin_center, fwhm)

def mean():
    
    print('----------------------------------------------------------------')
    
    print(r"\nMean $\chi_\text{reduced}^2$")
    
    n_dat = len(np.loadtxt('Data/M15_data_vel_U21.txt', skiprows=3)[:, 0])
    
    n_dof_E = n_dat-7
    
    n_dof_B = n_dat-6
    
    n_dof_Z = n_dat-9
    
    data = pd.read_csv('EINASTO/OutputMCMC_EINASTO.dat',\
                       delim_whitespace=True, skiprows=3)
    
    chi2_CLUMPY = data['chi2']
    
    chi2_true = -chi2_CLUMPY/2
    
    chi2_reduced = chi2_true/n_dof_E
    
    print(f'\nEINASTO: {np.mean(chi2_reduced)}')
    
    data = pd.read_csv('BURKERT/OutputMCMC_BURKERT.dat',\
                       delim_whitespace=True, skiprows=3)
    
    chi2_CLUMPY = data['chi2']
    
    chi2_true = -chi2_CLUMPY/2
    
    chi2_reduced = chi2_true/n_dof_B
    
    print(f'\nBURKERT: {np.mean(chi2_reduced)}')
    
    data = pd.read_csv('ZHAO/OutputMCMC_ZHAO.dat',\
                       delim_whitespace=True, skiprows=3)
    
    chi2_CLUMPY = data['chi2']
    
    chi2_true = -chi2_CLUMPY/2
    
    chi2_reduced = chi2_true/n_dof_Z
    
    print(f'\nZHAO:    {np.mean(chi2_reduced)}\n')
    
    print('----------------------------------------------------------------\n')


def average(model):
    
    start = 15
    
    stop = 95
    
    step = 5
    
    length = int((stop-start)/step)
    
    bins = np.linspace(start, stop, length+1)
    
    peaks = []
    
    FWHMs = []
    
    for i in range(len(bins)):
        
        joint_hist.joint_histogram(int(bins[i]))
        
        results = compare_models(model, int(bins[i]))
        
        peaks.append(results[0])
        
        FWHMs.append(results[1])
        
    mu_peaks = np.mean(peaks)
    
    std_peaks = np.std(peaks)
    
    mu_FWHMs = np.mean(FWHMs)
    
    std_FWHMs = np.std(FWHMs)
    
    print(f'\nModel: {model}\nPeak:  {mu_peaks:.5f}±{std_peaks:.5f}\nFWHM:  {mu_FWHMs:.5f}±{std_FWHMs:.5f}')
    
    return(mu_peaks, std_peaks, mu_FWHMs, std_FWHMs)

def main():
    
    comparison_plots.main()
    
    joint_rho.joint_rho()
    
    joint_J.joint_J()
    
    models = ['EINASTO', 'BURKERT', 'ZHAO']
    
    peak = []
    
    peak_std = []
    
    FWHM = []
    
    FWHM_std = []
    
    for i in range(len(models)):
        
        results = average(models[i])
        
        peak.append(results[0]-1)
        
        peak_std.append(results[1])
        
        FWHM.append(results[2])
        
        FWHM_std.append(results[3])
        
    peak_min = np.min(peak)
    
    FWHM_min = np.min(FWHM)
    
    j_peak = peak.index(peak_min)
    
    j_FWHM = FWHM.index(FWHM_min)
    
    print('\n----------------------------------------------------------------')
    
    if j_peak == j_FWHM:
        
        j = j_peak
        
        print(f'\nClosest peak to 1: {1+peak_min:.5f}±{peak_std[j]:.5f}\nSmallest FWHM:     {FWHM_min:.5f}±{FWHM_std[j]:.5f}\nBest model:        {models[j]}\n')
        
    else:
        
        print(f'\nClosest peak to 1: {1+peak_min}±{peak_std:.5f}\nCorresponds to {models[j_peak]} model.\nSmallest FWHM:  {FWHM_min:.5f}±{FWHM_std:.5f}\nCorresponds to {models[j_FWHM]} model.\n')
    
    mean()
    
    F_test.main()

if __name__ == "__main__":
    
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 15:50:49 2025

@author: Ivan
"""

import numpy as np
import pandas as pd
from scipy.stats import norm
from scipy import special

def z_test(data1, df1, data2, df2):
    """
    Perform a Z-test comparing two chi-square distributions.

    Parameters:
        data1 (array-like): Chi-square values for the first model.
        df1 (int): Degrees of freedom for the first model.
        data2 (array-like): Chi-square values for the second model.
        df2 (int): Degrees of freedom for the second model.

    Returns:
        z_stat (float): The Z-statistic.
        p_value (float): The p-value for the Z-test.
        sigma: sigma for the test.
    """
    # Calculate sample means
    mean1 = np.mean(data1)
    mean2 = np.mean(data2)
    
    # Calculate sample variances
    var1 = np.std(data1)**2
    var2 = np.std(data2)**2

    # Standard error for the difference in means
    se_diff = np.sqrt(var1/len(data1)+var2/len(data2))

    # Z-statistic
    z_stat = (mean1-mean2)/se_diff

    # Two-tailed p-value
    p_value = 2*(1-norm.cdf(abs(z_stat)))
    
    # Convert p-value to the number of sigma
    # For one-tailed p-value
    sigma = np.sqrt(2)*special.erfinv(1-p_value)

    return z_stat, p_value, sigma

def main():

    # Get the two chi-square distributions
    EINASTO = -pd.read_csv('EINASTO/OutputMCMC_EINASTO.dat',\
                               delim_whitespace=True, skiprows=3)['chi2']/2
    ZHAO = -pd.read_csv('ZHAO/OutputMCMC_ZHAO.dat', delim_whitespace=True,\
                               skiprows=3)['chi2']/2
    BURKERT = -pd.read_csv('BURKERT/OutputMCMC_BURKERT.dat',\
                           delim_whitespace=True, skiprows=3)['chi2']/2
    
    # Perform the Z-test
    df_EINASTO = len(EINASTO)-7
    df_ZHAO = len(ZHAO)-9
    df_BURKERT = len(BURKERT)-6
        
    # Perform pairwise Z-tests
    results = []
    pairs = [
             ("EINASTO vs BURKERT", EINASTO, df_EINASTO, BURKERT, df_BURKERT),
             ("ZHAO vs BURKERT", ZHAO, df_ZHAO, BURKERT, df_BURKERT),
             ("ZHAO vs EINASTO", ZHAO, df_ZHAO, EINASTO, df_EINASTO)
            ]
    
    for label, data1, df1, data2, df2 in pairs:
        z_stat, p_value, sigma = z_test(data1, df1, data2, df2)
        results.append((label, z_stat, p_value, sigma))
    
    # Print results
    print('\n----------------------------------------------------------------\n')
    for label, z_stat, p_value, sigma in results:
        print(f"{label}:")
        print(f"  Z-Statistic: {z_stat:.4f}")
        print(f"  P-Value:     {p_value:.4f}")
        print(f"  σ:           {sigma:.4f}\n")

if __name__ == "__main__":
    
    main()

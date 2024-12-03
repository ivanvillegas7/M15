#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 13:39:19 2024

@author: Ivan
"""

import numpy as np
import pandas as pd
from scipy.stats import f

def f_test(var1, var2, n1, n2, model1, model2):
    """
    Perform the F-test to compare two variances.
    Parameters:
    - var1: variance of the first model
    - var2: variance of the second model
    - n1: number of samples in the first model
    - n2: number of samples in the second model
    - model1: model 1
    - modle2: model 2
    
    Returns:
    - F_stat: calculated F statistic
    - p_value: p-value for the test
    """
    
    if model1=='EINASTO':
        
        n1 = n1 - 7
        
    if model2=='EINASTO':
        
        n2 = n2 - 7
        
    if model1=='BURKERT':
        
        n1 = n1 - 6
        
    if model2=='BURKERT':
        
        n2 = n2 - 6
        
    if model1=='ZHAO':
        
        n1 = n1 - 9
        
    if model2=='ZHAO':
        
        n2 = n2 - 9
    
    F_stat = (var1/n1)/(var2/n2)
    df1, df2 = n1 - 1, n2 - 1
    
    # Calculate the p-value
    p_value = 2 * min(f.cdf(F_stat, df1, df2), 1 - f.cdf(F_stat, df1, df2))
    
    return F_stat, p_value

def compare_models_chi2(chi2_values_list):
    """
    Perform pairwise F-tests between three models based on chi-squared values.
    Parameters:
    - chi2_values_list: list of arrays, where each array contains chi-squared
                        values for a model
    
    Returns:
    - results: dictionary containing F-statistics and p-values for each model
               pair
    """
    results = {}
    model_names = ["EINASTO", "BURKERT", "ZHAO"]
    
    # Calculate variances and sample sizes
    variances = [np.var(chi2) for chi2 in chi2_values_list]
    sample_sizes = [len(chi2) for chi2 in chi2_values_list]
    
    # Perform pairwise F-tests between the models
    for i in range(3):
        for j in range(i + 1, 3):
            F_stat, p_value = f_test(variances[i], variances[j],\
                                     sample_sizes[i], sample_sizes[j],\
                                     model_names[i], model_names[j])
            results[f"{model_names[i]} vs {model_names[j]}"] = {"F-statistic": F_stat, "p-value": p_value}
    
    return results

def main():

    EINASTO = -pd.read_csv('EINASTO/OutputMCMC_EINASTO.dat',\
                           delim_whitespace=True, skiprows=3)['chi2']/2
    
    BURKERT = -pd.read_csv('BURKERT/OutputMCMC_BURKERT.dat',\
                           delim_whitespace=True, skiprows=3)['chi2']/2
        
    ZHAO = -pd.read_csv('ZHAO/OutputMCMC_ZHAO.dat', delim_whitespace=True,\
                           skiprows=3)['chi2']/2
    
    # Run the F-test comparisons
    results = compare_models_chi2([EINASTO, BURKERT, ZHAO])
    
    # Print the results
    for model_pair, stats in results.items():
        print(f"\n{model_pair}: F-statistic = {stats['F-statistic']:.4f}, p-value = {stats['p-value']:.4f}")
        
main()

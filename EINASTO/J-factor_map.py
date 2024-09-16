#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 18:05:20 2024

@author: ivan
"""

import healpy as hp

from astropy.io import fits

from matplotlib import pyplot as plt

import numpy as np

import scipy.interpolate

import scipy.integrate


def CLUMPYmaps():

    outfile = 'Results/output/annihil_M152D_FOVdiameter4.0deg_nside1024.fits'
    
    ext = 3  # fluxes and intensities

    col = 3  # gamma-ray intensity

    data = hp.read_map(outfile, partial=True, hdu=ext, field=col-1)

    hdulist = fits.open(outfile)

    dtheta = hdulist[ext].header['SIZE_Y']

    dtheta_orth = hdulist[ext].header['SIZE_X']

    hdulist.close()

    hp.cartview(data, lonra=[-dtheta_orth/2, dtheta_orth/2],
                latra=[-dtheta/2, dtheta/2], norm='log', max=data.max()/10,
                title=r'$\gamma$-intensity', unit=r'cm$^{-2}$ s$^{-1}$ sr$^{-1}$')

    plt.savefig('Results/Intensity_gamma.pdf')
    
    ext_ = 2 # dJ/dOmega
    
    col_ = 1 # smooth DM only
    
    data = hp.read_map(outfile, partial=True, hdu=ext_, field=col_-1)
    
    hp.cartview(data, lonra=[-dtheta_orth/2,dtheta_orth/2],\
                latra=[-dtheta/2,dtheta/2], norm='log', title=r'$dJ/d\Omega$',
                unit=r'GeV$^2$ cm$^{-5}$ sr$^{-1}$')

    plt.savefig('Results/J_per_sr.pdf')


def integrate_CC(threshold):
    
    # Load data
    data = np.loadtxt('Results/output/annihil_M152D_FOVdiameter4.0deg_nside1024-INTEGRATED_FLUXES.dat')
    x = data[:, 0]*np.pi/180
    y = data[:, 1]*np.pi/180
    f_xy = data[:, 4]
    
    # Convert to polar coordinates
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)
    
    # Create a grid for interpolation
    r_max = np.max(r)
    r_grid = np.linspace(0, r_max, 500)
    theta_grid = np.linspace(0, 2 * np.pi, 500)
    r_grid, theta_grid = np.meshgrid(r_grid, theta_grid)
    
    # Interpolate f(r, theta) on the grid using nearest method initially to avoid NaNs
    f_grid_nearest = scipy.interpolate.griddata((r, theta), f_xy, (r_grid, theta_grid), method='nearest')
    
    # Interpolate again using a more sophisticated method where possible
    f_grid = scipy.interpolate.griddata((r, theta), f_xy, (r_grid, theta_grid), method='cubic')
    
    # Fill NaN values in f_grid with values from the nearest-neighbor interpolation
    nan_mask = np.isnan(f_grid)
    f_grid[nan_mask] = f_grid_nearest[nan_mask]
    
    # Define the integrand in polar coordinates
    def integrand(r, theta):
        return scipy.interpolate.griddata((r_grid.flatten(), theta_grid.flatten()), f_grid.flatten(), (r, theta), method='nearest') * r
    
    # Calculate the total integral over the entire domain using Simpson's rule
    r_values = np.linspace(0, r_max, 1000)
    theta_values = np.linspace(0, 2 * np.pi, 1000)
    R, Theta = np.meshgrid(r_values, theta_values)
    F = integrand(R, Theta)
    
    # Perform the double integral using Simpson's rule
    total_signal = scipy.integrate.simpson(scipy.integrate.simpson(F, theta_values, axis=0), r_values)
    
    # Incremental integration to find X% of the total signal
    cumulative_signal = 0.0
    r_index = 0
    
    while cumulative_signal < threshold * total_signal and r_index < len(r_values):
        partial_signal = scipy.integrate.simpson(F[:, r_index], theta_values)
        cumulative_signal += partial_signal
        r_index += 1
    
    # Print the radius at which we reach X% of the total signal
    r_X_percent = r_values[r_index - 1]
    print("DM model: EINASTO\n")
    print(f"Radius at which {100*threshold}% of the total signal is reached: {r_X_percent*180/np.pi} degrees.")
    print(f"Cumulative signal at this radius: {cumulative_signal} (should be close to {threshold * total_signal}).")
    
def no_integration(threshold):
    
    """
    sum column 3 (2 in python)
    find (0, 0)
    sort on one angle direction and the other one follows, as well as the flux
    sum from (0, 0) to (ndx, ndy) until reaching X% of first sum
    """
    
    # Load data
    data = np.loadtxt('Results/output/annihil_M152D_FOVdiameter4.0deg_nside1024-INTEGRATED_FLUXES.dat')
    x = data[:, 0]*np.pi/180
    y = data[:, 1]*np.pi/180
    signal = data[:, 2]
    
    # Calculate the total signal
    total_signal = np.sum(signal)

    # Calculate distance from the origin (0, 0)
    distances = np.sqrt(x**2 + y**2)
    
    # Combine the data into a structured array for sorting
    structured_data = np.core.records.fromarrays([x, y, signal, distances],
                                                 names='x, y, signal, distance')
    
    # Sort the structured array by distance from the origin
    sorted_data = np.sort(structured_data, order='distance')
    
    # Function to sum values in concentric circles until reaching X% of the total signal
    def sum_concentric_circles(sorted_data, total_signal, threshold):
        target_signal = total_signal * threshold
        cumulative_sum = 0
        circle_data = []
        
        for point in sorted_data:
            cumulative_sum += point['signal']
            circle_data.append((point['x'], point['y'], cumulative_sum, point['distance']))
            if cumulative_sum >= target_signal:
                break
        
        return circle_data
    
    # Get the data within the required percentage of the total signal
    circle_data = sum_concentric_circles(sorted_data, total_signal, threshold)
    
    # Display the results
    for data in circle_data:
        print(f"Coordinate: ({data[0]*180/np.pi}, {data[1]*180/np.pi}), Cumulative Value: {data[2]}\n\n")
        
    # Print the radius of the last circle
    if circle_data:
        last_radius = circle_data[-1][3]
        print(f"Radius of the last circle: {last_radius*180/np.pi} degrees.")



def main():

    CLUMPYmaps()

    #integrate_CC(0.95)
    
    no_integration(0.95)

main()

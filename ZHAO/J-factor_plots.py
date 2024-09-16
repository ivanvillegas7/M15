# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

def main():
    
    data = np.loadtxt('Results/output/OutputMCMC_ZHAO.dat.Jalphaint_cls.output',\
                      skiprows=3)
    
    plt.figure()
    plt.plot(data[:, 0], data[:, 1], color='black', label='Median')
    plt.plot(data[:, 0], data[:, 5], color='blue')
    plt.plot(data[:, 0], data[:, 6], color='blue')
    plt.fill_between(data[:, 0], data[:, 5], data[:, 6], label=r'$65\%$ CL',\
                     color='lightblue')
    plt.plot(data[:, 0], data[:, 7], color='orange')
    plt.plot(data[:, 0], data[:, 8], color='orange')
    plt.fill_between(data[:, 0], data[:, 7], data[:, 5], label=r'$95\%$ CL',\
                     color='wheat')
    plt.fill_between(data[:, 0], data[:, 6], data[:, 8], color='wheat')
    (ymin, ymax) = (1e22, 1e27)
    plt.vlines(0.1, ymin, ymax, color='red', ls='dotted',\
               label=r'$\alpha=0.1^\text{o}$')
    plt.vlines(0.35, ymin, ymax, color='darkslategray', ls='dotted',\
               label=r'$\alpha(R_t=0.067\text{ kpc})=0.35^\text{o}$')
    plt.vlines(0.5, ymin, ymax, color='green', ls='dashed',\
               label=r'$\alpha=0.5^\text{o}$')
    plt.xlabel(r'$\alpha_\text{int}$ [deg]')
    plt.ylabel(r'$J(\alpha_\text{int})$ [GeV$^2$ cm$^{-5}$]')
    plt.title(r"M15's $J$-factor")
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.xscale('log')
    plt.yscale('log')
    plt.xlim(1e-2, 2)
    plt.ylim(ymin, ymax)
    plt.savefig('Results/J-factor_all_combined.pdf')
    
    plt.figure()
    plt.plot(data[:, 0], data[:, 1], color='black', label='Median')
    plt.plot(data[:, 0], data[:, 5], color='blue')
    plt.plot(data[:, 0], data[:, 6], color='blue')
    plt.fill_between(data[:, 0], data[:, 5], data[:, 6], label=r'$65\%$ CL',\
                     color='lightblue')
    plt.plot(data[:, 0], data[:, 7], color='orange')
    plt.plot(data[:, 0], data[:, 8], color='orange')
    plt.fill_between(data[:, 0], data[:, 7], data[:, 5], label=r'$95\%$ CL',\
                     color='wheat')
    plt.fill_between(data[:, 0], data[:, 6], data[:, 8], color='wheat')
    (ymin, ymax) = (plt.ylim()[0], 1e27)
    plt.vlines(0.1, ymin, ymax, color='red', ls='dashed',\
               label=r'$\alpha=0.1^\text{o}$')
    plt.vlines(0.5, ymin, ymax, color='green', ls='dashed',\
               label=r'$\alpha=0.5^\text{o}$')
    plt.plot(4.56e-5, 7.5e18, marker='X', label='H.E.S.S.', ls='none',\
             color='black')
    plt.plot(4.56e-5, 2.15e22, marker='X', ls='none', color='black')
    plt.plot(4.56e-5, 7e19, marker='X', ls='none', color='black')
    plt.vlines(0.0005, 2.457e16, 5.2648e17, label='Whipple', color='brown')
    plt.hlines(2.457e16, 0.00055, 0.00045, color='brown')
    plt.hlines(5.2648e17, 0.00055, 0.00045, color='brown')
    plt.vlines(0.0005, 2.81e19, 7.02e19, color='brown')
    plt.hlines(2.81e19, 0.00055, 0.00045, color='brown')
    plt.hlines(7.02e19, 0.00055, 0.00045, color='brown')
    plt.xlabel(r'$\alpha_\text{int}$ [deg]')
    plt.ylabel(r'$J(\alpha_\text{int})$ [GeV$^2$ cm$^{-5}$]')
    plt.title(r"M15's $J$-factor")
    plt.legend(loc='lower center')
    plt.grid(True)
    plt.xscale('log')
    plt.yscale('log')
    plt.xlim(4e-5, 5)
    plt.ylim(ymin, ymax)
    plt.savefig('Results/J-factor_all_combined_long.pdf')
    
main()

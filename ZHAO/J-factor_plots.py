# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import transform_abramowski
import transform_wood

def main():
    
    data = np.loadtxt('Results/output/OutputMCMC_ZHAO.dat.Jalphaint_cls.output',\
                      skiprows=3)
    
    plt.figure()
    plt.plot(data[:, 0], data[:, 1], color='black', label='Median')
    plt.plot(data[:, 0], data[:, 5], color='blue')
    plt.plot(data[:, 0], data[:, 6], color='blue')
    plt.fill_between(data[:, 0], data[:, 5], data[:, 6], label=r'$68\%$ CL',\
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
    plt.legend()
    plt.grid(True)
    plt.xscale('log')
    plt.yscale('log')
    plt.xlim(1e-3, 2)
    plt.ylim(ymin, ymax)
    plt.savefig('Results/J-factor_all_combined.pdf')
    
    J_Wood=transform_wood.main()
    
    J_Abramowski=transform_abramowski.main()
    
    plt.figure()
    plt.plot(data[:, 0], data[:, 1], color='black', label='Median')
    plt.plot(data[:, 0], data[:, 5], color='blue')
    plt.plot(data[:, 0], data[:, 6], color='blue')
    plt.fill_between(data[:, 0], data[:, 5], data[:, 6], label=r'$68\%$ CL',\
                     color='lightblue')
    plt.plot(data[:, 0], data[:, 7], color='orange')
    plt.plot(data[:, 0], data[:, 8], color='orange')
    plt.fill_between(data[:, 0], data[:, 7], data[:, 5], label=r'$95\%$ CL',\
                     color='wheat')
    plt.fill_between(data[:, 0], data[:, 6], data[:, 8], color='wheat')
    (ymin, ymax) = (1e18, 1e28)
    plt.vlines(0.1, ymin, ymax, color='red', ls='dashed',\
               label=r'$\alpha=0.1^\text{o}$')
    plt.vlines(0.5, ymin, ymax, color='green', ls='dashed',\
               label=r'$\alpha=0.5^\text{o}$')
    plt.plot(0.07228242712521225, J_Abramowski[0], marker='X', label='H.E.S.S.', ls='none',\
             color='black')
    plt.plot(0.07228242712521225, J_Abramowski[1], marker='X', ls='none', color='black')
    plt.plot(0.07228242712521225, J_Abramowski[2], marker='X', ls='none', color='black')
    plt.vlines(0.2503938552031453, J_Wood[0], J_Wood[1], label='Whipple', color='brown')
    plt.hlines(J_Wood[0], 0.3, 0.21, color='brown')
    plt.hlines(J_Wood[1], 0.3, 0.21, color='brown')
    plt.vlines(0.2503938552031453, J_Wood[2], J_Wood[3], color='brown')
    plt.hlines(J_Wood[2], 0.3, 0.21, color='brown')
    plt.hlines(J_Wood[3], 0.3, 0.21, color='brown')

    plt.xlabel(r'$\alpha_\text{int}$ [deg]')
    plt.ylabel(r'$J(\alpha_\text{int})$ [GeV$^2$ cm$^{-5}$]')
    plt.title(r"M15's $J$-factor")
    plt.legend()
    plt.grid(True)
    plt.xscale('log')
    plt.yscale('log')
    plt.xlim(1e-3, 5)
    plt.ylim(ymin, ymax)
    plt.savefig('Results/J-factor_all_combined_long.pdf')
    
main()

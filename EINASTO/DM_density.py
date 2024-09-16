# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
    
def main():
    
    #data = np.loadtxt('Results/output/OutputMCMC.dat.rhor_cls.output',\
    data = np.loadtxt('Results/output/OutputMCMC_Burkert.dat.rhor_cls.output',\
                      skiprows=3)
    plt.figure()
    plt.plot(1e3*data[:, 0], 1e-9*data[:, 1], color='black')
    plt.plot(1e3*data[:, 0], 1e-9*data[:, 5], color='blue')
    plt.plot(1e3*data[:, 0], 1e-9*data[:, 6], color='blue')
    plt.fill_between(1e3*data[:, 0], 1e-9*data[:, 5], 1e-9*data[:, 6],\
                     label=r'$65\%$ CL', color='lightblue')
    plt.plot(1e3*data[:, 0], 1e-9*data[:, 7], color='orange')
    plt.plot(1e3*data[:, 0], 1e-9*data[:, 8], color='orange')
    plt.fill_between(1e3*data[:, 0], 1e-9*data[:, 7], 1e-9*data[:, 5],\
                     label=r'$95\%$ CL', color='wheat')
    plt.fill_between(1e3*data[:, 0], 1e-9*data[:, 6], 1e-9*data[:, 8],\
                     color='wheat')
    plt.vlines(1e3*0.044, 1e-3, 1e8, ls='dashdot',\
               label=r'$r=044\text{ pc}$', color='grey')
    plt.vlines(1e3*0.058, 1e-3, 1e86, ls='dashdot',\
               label=r'$r=58\text{ pc}$', color='red')
    plt.vlines(1e3*0.067, 1e-3, 1e8, ls='dashdot',\
               label=r'$r=67\text{ pc}$', color='green')
    plt.vlines(1e3*0.080, 1e-3, 1e8, ls='dashdot',\
               label=r'$r=80\text{ pc}$', color='purple')    
    plt.xlabel(r'$r$ [pc]')
    plt.ylabel(r'$\rho_\text{DM}(r)$ [$M_\odot$ pc$^{-3}$]')
    plt.title("M15's dark matter density")
    plt.legend(loc='lower left')
    plt.grid(True)
    plt.xscale('log')
    plt.yscale('log')
    plt.xlim(1e-3, 1e3)
    plt.ylim(1e-3, 1e8)
    plt.savefig('Results/DM_density_CL.pdf')
    
main()

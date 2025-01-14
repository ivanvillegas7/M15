# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

def all_J():

    files: list[str] = ['044', '058', '067', '080']
    
    colors: list[str] = ['blue', 'green', 'red', 'purple']
    
    plt.figure()
    
    for i in range(len(files)):
        
        data = np.loadtxt(f'Results/output/OutputMCMC_{files[i]}.dat.Jalphaint_cls.output',\
                          skiprows=3)
            
        plt.plot(data[:, 0], data[:, 1], color=colors[i],\
                 label=f'Median for r=0.{files[i]} kpc', linewidth=3.0)
        plt.plot(data[:, 0], data[:, 5], color=colors[i], ls='dashed',\
                 label=r'$68\%$ CL', linewidth=3.0)
        plt.plot(data[:, 0], data[:, 6], color=colors[i], ls='dashed',\
                 linewidth=3.0)
        plt.plot(data[:, 0], data[:, 7], color=colors[i], ls='dotted',\
                 label=r'$95\%$ CL', linewidth=3.0)
        plt.plot(data[:, 0], data[:, 8], color=colors[i], ls='dotted',\
                 linewidth=3.0)
    
    plt.vlines(0.1, plt.ylim()[0], plt.ylim()[1], ls='dashdot',\
               label=r'$\alpha_\text{int}=0.1^\text{o}$', color='black',\
                   linewidth=3.0)
    plt.vlines(0.5, plt.ylim()[0], plt.ylim()[1], ls='dashdot',\
               label=r'$\alpha_\text{int}=0.5^\text{o}$', color='grey',\
                   linewidth=3.0)     
    plt.xlabel(r'$\alpha_\text{int}$ [deg]')
    plt.ylabel(r'$J(\alpha_\text{int})$ [GeV$^2$ cm$^{-5}$]')
    plt.legend()
    #plt.legend(loc="upper left", bbox_to_anchor=(1, 1))
    #plt.tight_layout()
    plt.grid(True)
    plt.xscale('log')
    plt.yscale('log')
    plt.xlim(1e-2, 2)
    plt.savefig('Results/J-factor_all.pdf')
    
def combined_data():
    
    data = np.loadtxt('Results/output/OutputMCMC.dat.Jalphaint_cls.output',\
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
    plt.vlines(0.23, ymin, ymax, color='purple', ls='dashed',\
               label=r'$\alpha(R_t=44\text{ pc})=0.23^\text{o}$')
    plt.vlines(0.3, ymin, ymax, color='pink', ls='dotted',\
               label=r'$\alpha(R_t=58\text{ pc})=0.3^\text{o}$')
    plt.vlines(0.35, ymin, ymax, color='darkslategray', ls='dotted',\
               label=r'$\alpha(R_t=67\text{ pc})=0.35^\text{o}$')
    plt.vlines(0.42, ymin, ymax, color='gold', ls='dotted',\
               label=r'$\alpha(R_t=80\text{ pc})=0.42^\text{o}$')
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
    plt.vlines(0.23, ymin, ymax, color='purple', ls='dotted',\
               label=r'$\alpha=0.23^\text{o}$')
    plt.vlines(0.3, ymin, ymax, color='pink', ls='dotted',\
               label=r'$\alpha=0.3^\text{o}$')
    plt.vlines(0.35, ymin, ymax, color='darkslategray', ls='dotted',\
               label=r'$\alpha=0.35^\text{o}$')
    plt.vlines(0.42, ymin, ymax, color='gold', ls='dotted',\
               label=r'$\alpha=0.42^\text{o}$')
    plt.vlines(0.5, ymin, ymax, color='green', ls='dashed',\
               label=r'$\alpha=0.5^\text{o}$')
    plt.plot(0.07228242712521225, 7.5e18, marker='X', label='H.E.S.S.', ls='none',\
             color='black')
    plt.plot(0.07228242712521225, 2.15e22, marker='X', ls='none', color='black')
    plt.plot(0.07228242712521225, 7e19, marker='X', ls='none', color='black')
    plt.vlines(0.2503938552031453, 2.457e16, 5.2648e17, label='Whipple', color='brown')
    plt.hlines(2.457e16, 0.3, 0.21, color='brown')
    plt.hlines(5.2648e17, 0.3, 0.21, color='brown')
    plt.vlines(0.2503938552031453, 2.81e19, 7.02e19, color='brown')
    plt.hlines(2.81e19, 0.3, 0.21, color='brown')
    plt.hlines(7.02e19, 0.3, 0.21, color='brown')
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
    
def main():
    
    all_J()
    
    combined_data()
    
main()

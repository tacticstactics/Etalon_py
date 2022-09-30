
#Etalon_Power_Basic_def

import numpy as np
import math

def proc1(param, m):

    global c
    c = 2.99792458E+14 # um / s

    wl0 = 0.65; #um
    etalen = 1000; #um

    stepwl = 0.5*wl0**2/(etalen * m); # um

    print('')
    print('stepwl = ', stepwl)


    wlcol = np.zeros(m); # wavelength

    omegacol = np.zeros(m); # wavelength

    PTetacol = np.zeros(m); # PowerTrans
    
    PRetacol = np.zeros(m); # PowerReflection

    #Etcol = np.ones(m, dtype=complex);#*2
       
    #Signalcol = np.ones(m, dtype=complex);#*2

    Re1 = 0.95;
    Re2 = 0.99;

    re1 = math.sqrt(Re1);
    re2 = math.sqrt(Re2);
    te1 = math.sqrt(1-Re1);
    te2 = math.sqrt(1-Re2);
    
    for ii in range(m):


        wl = wl0 + ii * stepwl
        wlcol[ii] = wl

        omega = 2 * math.pi * c / wl;
        omegacol[ii] = omega

        Et = -1*(te1*te2)*np.exp(-1j * 4 * math.pi * etalen /wl) / (1 - re1*re2 * np.exp(-1j * 2*4 * math.pi * etalen /wl));
        
        conjEt = Et.conjugate()
        PT = Et * conjEt
        PTetacol[ii] = PT
        

        PR = 1-PT
        PRetacol[ii] = PR
        


    return wlcol, PTetacol,PRetacol



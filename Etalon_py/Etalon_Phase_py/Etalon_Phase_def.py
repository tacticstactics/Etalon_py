
#Etalon_Phase_def

import numpy as np
import math
import cmath

def proc1(param=0.01,m=512):

    global c
    c = 2.99792458E+14 # um / s

    stepwl = 0.000003; # um
    wl0 = 0.65; #um

    wlcol = np.zeros((m,1)); # wavelength

    omegacol = np.zeros((m,1)); # wavelength

    PTetacol = np.zeros((m,1)); # PowerTrans
    
    PRetacol = np.zeros((m,1)); # PowerReflection

    Etphasecol = np.zeros((m,1)); # Phase of Trans E

    Erphasecol = np.zeros((m,1)); # Phase of Refleced E
       
    #Signalcol = np.ones(m, dtype=complex);#*2

    Re1 = 0.9001;
    Re2 = 0.9001;

    re1 = math.sqrt(Re1);
    re2 = math.sqrt(Re2);
    te1 = math.sqrt(1-Re1);
    te2 = math.sqrt(1-Re2);

    etalen = 1500;
    

    for ii in range(m):

        wl = wl0 + ii * stepwl
        wlcol[(ii)] =wl

        omega = 2 * math.pi * c / wl;
        omegacol[(ii)] = omega

        # Unknown Resource
        #Et = (te1*te2)*np.exp(-1j * 4 * math.pi * etalen /wl) / (1+re1*re2 * np.exp(-1j * 4 * math.pi * etalen /wl));
        
        # yariv, page.135
        
        Er = re1+(te1*te2*re2)*np.exp(1j*4*math.pi*etalen/wl)*(1+re2*re2*np.exp(1j*4*math.pi*etalen/wl)+re2*re2*re2*re2*np.exp(1j*2*4*math.pi*etalen/wl));
        Et = (te1*te2)*(1+re2*re2*np.exp(1j*4*math.pi*etalen/wl)+re2*re2*re2*re2*np.exp(1j*2*4*math.pi*etalen/wl));
        

        conjEt = Et.conjugate()
        PT = Et * conjEt

        Etphase = cmath.phase(Et)
        Etphasecol[(ii)] = Etphase

        PTetacol[(ii)] =PT

        conjEr = Er.conjugate()
        PR = Er * conjEr
        PRetacol[(ii)] = PR

        Erphase = cmath.phase(Er)
        Erphasecol[(ii)] = Erphase



        


    return wlcol, PTetacol, PRetacol, Etphasecol, Erphasecol


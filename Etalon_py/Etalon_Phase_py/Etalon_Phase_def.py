
#Etalon_Phase_def.py

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

    # PRe1 must be higher than or equal to PRe2 because this air to glass incidence was assumed here.

    PRe1 = 0.501;
    PRe2 = 0.501;

    # Consider Glass Etalon, e.g.Air to glass.
    # sign of re1 is negative. due to Phase jump
    # sign of re2 is positive
    # sign of te1 is positive
    # sign of te2 is positive

    
    re1 = -1 * math.sqrt(PRe1);
    print('re1 = ',re1)

    
    re2 = math.sqrt(PRe2);
    print('re2 = ',re2)


    te1 = math.sqrt(1-PRe1);
    print('te1 = ',te1)

    te2 = math.sqrt(1-PRe2);
    print('te2 = ',te2)

    etalen = 500; # Etalon Length in um
    

    for ii in range(m):

        wl = wl0 + ii * stepwl
        wlcol[(ii)] =wl

        omega = 2 * math.pi * c / wl;
        omegacol[(ii)] = omega

        sigma = 4*math.pi*etalen/wl # Phase change ver each return

        # Yariv, Optoelectronics, page.135
        
        Er = re1+(te1*te2*re2)*np.exp(1j*sigma)*(1+re2**2*np.exp(1j*1*sigma)+re2**4*np.exp(1j*2*sigma)+re2**6*np.exp(1j*3*sigma)+re2**8*np.exp(1j*4*sigma)+re2**10*np.exp(1j*5*sigma));
        Et = (te1*te2)*(1+re2**2*np.exp(1j*1*sigma)+re2**4*np.exp(1j*2*sigma)+re2**6*np.exp(1j*3*sigma)+re2**8*np.exp(1j*4*sigma)+re2**10*np.exp(1j*5*sigma));
        

        #Reflect
        #conjEr = Er.conjugate()
        PR = abs(Er)**2
        PRetacol[(ii)] = PR

        Erphase = cmath.phase(Er)
        Erphasecol[(ii)] = Erphase
        
        #Trans
        #conjEt = Et.conjugate()
        PT = abs(Et)**2
        PTetacol[(ii)]=PT

        Etphase = cmath.phase(Et)
        Etphasecol[(ii)] = Etphase     


    return wlcol, PTetacol, PRetacol, Etphasecol, Erphasecol



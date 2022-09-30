
#Etalon_Phase_def.py

import numpy as np
import math
import cmath

def proc1(param, m):

    global c
    c = 2.99792458E+14 # um / s



    wl0 = 0.65; #um
    etalen = 1000; # Etalon Length in um

    stepwl = wl0**2/(etalen * m); # um
    
    print('stepwl = ',stepwl)

    # PRe1 must be higher than or equal to PRe2 because this air to glass incidence was assumed here.

    PRe1 = 0.801;
    PRe2 = 0.801;


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


    wlcol = np.zeros(m); # wavelength
    omegacol = np.zeros(m); # wavelength
    PTetacol = np.zeros(m); # PowerTrans    
    PRetacol = np.zeros(m); # PowerReflection
    Etphasecol = np.zeros(m); # Phase of Trans E
    Erphasecol = np.zeros(m); # Phase of Refleced E  
       

    for ii in range(m):

        wl = wl0 + ii * stepwl
        wlcol[ii] = wl

        omega = 2 * math.pi * c / wl;
        omegacol[ii] = omega

        sigma = 4*math.pi*etalen/wl # Phase change per each round trip

        # Yariv, Optoelectronics, page.135
        
        Er = re1+(te1*te2*re2)*np.exp(1j*sigma)*(1+re2**2*np.exp(1j*1*sigma)+re2**4*np.exp(1j*2*sigma)+re2**6*np.exp(1j*3*sigma)+re2**8*np.exp(1j*4*sigma) + \
            re2**10*np.exp(1j*5*sigma)+re2**12*np.exp(1j*6*sigma) + re2**14*np.exp(1j*7*sigma) + re2**16*np.exp(1j*8*sigma) + re2**18*np.exp(1j*9*sigma) + \
            re2**20*np.exp(1j*10*sigma) + re2**22*np.exp(1j*11*sigma));


        Et = (te1*te2)*(1+re2**2*np.exp(1j*1*sigma)+re2**4*np.exp(1j*2*sigma)+re2**6*np.exp(1j*3*sigma)+re2**8*np.exp(1j*4*sigma)+ \
            re2**10*np.exp(1j*5*sigma)+re2**12*np.exp(1j*6*sigma) + re2**14*np.exp(1j*7*sigma) + re2**16*np.exp(1j*8*sigma) + re2**18*np.exp(1j*9*sigma) + \
            re2**20*np.exp(1j*10*sigma) + re2**22*np.exp(1j*11*sigma));
        

        #Reflect
        #conjEr = Er.conjugate()
        PR = abs(Er)**2
        PRetacol[ii] = PR

        Erphase = cmath.phase(Er)
        Erphasecol[ii] = Erphase
        
        #Trans
        #conjEt = Et.conjugate()
        PT = abs(Et)**2
        PTetacol[ii]=PT

        Etphase = cmath.phase(Et)
        Etphasecol[ii] = Etphase     


    return wlcol, PTetacol, PRetacol, Etphasecol, Erphasecol



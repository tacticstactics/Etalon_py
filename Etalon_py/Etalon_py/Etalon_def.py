
#Etalon_def

import numpy as np


def proc1(param=0.01,m=256):

    stepwl = 0.0001; # um
    wl0 = 0.65; #um

    wlcol = np.zeros((m,1)); # wavelength
    
    PTetacol = np.zeros((m,1)); # PowerTrans
    
    PRetacol = np.zeros((m,1)); # PowerReflection

    #Etcol = np.ones(m, dtype=complex);#*2
       
    #Signalcol = np.ones(m, dtype=complex);#*2


    freq = 4
    omega = 2*np.pi*freq
 
    print('omega=', omega, 'Hz')

    #Pulsewidth
    tau = 0.4 

    # PD signal. Proportional to optical power
    #Signal = 0


    for ii in range(m):


        wl = wl0 + ii * stepwl

        wlcol[(ii)] =wl

        PT = 1

        PTetacol[(ii)] =PT

        PR = 1

        PRetacol[(ii)] = PR
        


    return wlcol, PTetacol,PRetacol



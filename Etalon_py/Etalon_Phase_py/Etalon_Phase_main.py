
#Etalon_Phase_main.py




import numpy as np
import matplotlib.pyplot as plt

import Etalon_Phase_def

param = 0.01
m = 128

wlcol, PTetacol,PRetacol = Etalon_Phase_def.proc1(param,m)


print('')
print('Etalon_Phase_main.py')
print('')


fig = plt.figure(figsize = (10,6), facecolor='lightblue')

ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)

ax1.plot(wlcol,PTetacol)
ax2.plot(wlcol,PRetacol)
#ax3.plot(wlcol,np.real(Signalcol))

plt.show()

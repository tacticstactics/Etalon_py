
#Etalon_Power_main.py


import matplotlib.pyplot as plt

import Etalon_Power_def


param = 0.01
m = 128

wlcol, PTetacol,PRetacol = Etalon_Power_def.proc1(param,m)


print('')
print('Etalon_Power_main.py')
print('Phase Information is not given.')
print('')


fig = plt.figure(figsize = (10,6), facecolor='lightblue')

ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2, sharey=ax1)

ax1.plot(wlcol,PTetacol)
ax1.set_xlabel("Wavelength")
ax1.set_ylabel("Transmission")
ax1.set_ylim(0,2)

ax2.plot(wlcol,PRetacol)
ax2.set_xlabel("Wavelength")
ax2.set_ylabel("Reflection")
ax2.set_ylim(0,2)

plt.show()

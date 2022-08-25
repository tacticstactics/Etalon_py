
#Etalon_Power_main.py


import matplotlib.pyplot as plt

import Etalon_Power_def


param = 0.01
m = 128

wlcol, PTetacol,PRetacol = Etalon_Power_def.proc1(param,m)


print('')
print('Etalon_Power_main.py')
print('')


fig = plt.figure(figsize = (10,6), facecolor='lightblue')

ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2, sharey=ax1)

ax1.plot(wlcol,PTetacol)
ax2.plot(wlcol,PRetacol)

plt.show()

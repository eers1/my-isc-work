import matplotlib.pyplot as plt
import numpy as np


Time = [0, 1, 2, 3, 4, 5, 6]
CO2conc = [250, 265, 272, 260, 300, 320, 389]
Temp = [14.1, 15.5, 16.3, 18.1, 17.3, 19.1, 20.2]

fig, ax1 = plt.subplots()

ax1.plot(Time, CO2conc, '--b')
ax1.set_ylabel('CO2 Concentration (ppm)')

ax2 = ax1.twinx()
ax2.plot(Time, Temp, 'r')
ax2.set_ylabel('Temp (degC)')

plt.title('Itty Bitty Pretty Chemistry Thang')
plt.xlabel('Time (decade)')

plt.pause(3)



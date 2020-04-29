import matplotlib.pyplot as plt
import numpy as np
import serial
import time

tilt = np.arange(0,10,0.1)

serdev = '/dev/ttyACM0'
s = serial.Serial(serdev,115200)
#line=s.readline() # Read an echo string from K66F terminated with '\n'
for i in range(0, int(100)):
    line=s.readline() # Read an echo string from K66F terminated with '\n'
    # print line
    tilt[i] = float(line)    


fig, ax = plt.subplots(1, 1)
for i in range(0, 100) :
    ax.plot([i/10, i/10], [0, tilt[i]], color = 'blue', linewidth = 1, linestyle="-") 
    ax.scatter([i/10,], [tilt[i],], 70, color = 'blue')
ax.plot([0, 10], [0, 0], color = "red", linewidth = 1, linestyle = "-")
ax.set_xlabel('Time')
ax.set_ylabel('over_5_cm')
plt.show()
s.close()
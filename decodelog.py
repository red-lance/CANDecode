import matplotlib.pyplot as plt
import numpy as np

logfile = open("dta.csv", "r")
s1c1 = []
s1c2 = []
s1c3 = []
s1c4 = []
count = 0
for a in logfile.readlines():
    b = a.split(",")

    if b[0] =="6A":
        data = b[1:len(b)]
        data[-1] = '7E'
        crr_data = data[::-1]

        for i in range(0, len(crr_data)-1, 2):
            a = crr_data[i]+crr_data[i+1]
            value = int(a, 16)*0.0001
            if i<2:
                s1c1.append(value)
            elif i<4:
                s1c2.append(value)
            elif i<6:
                s1c3.append(value)
            else:
                s1c4.append(value)
        
print()


yc1 = np.array(s1c1)
yc2 = np.array(s1c2)
yc3 = np.array(s1c3)
yc4 = np.array(s1c4)
plt.plot(yc1)
plt.plot(yc2, linestyle = 'dashed')
plt.plot(yc3, linestyle = 'dotted')
plt.plot(yc4, linestyle = 'dashdot')
plt.show()

       
            



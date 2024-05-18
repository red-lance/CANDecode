import matplotlib.pyplot as plt
import numpy as np

logfile = open("dta.csv", "r")
ids = ["6B", "69", "6A"]
s1c1 = []
s1c2 = []
s1c3 = []
s1c4 = []
s1c5 = []
s1c6 = []
s1c7 = []
s1c8 = []
s1c9 = []
s1c10 = []
s1c11 = []
s1c12 = []

for a in logfile.readlines():
    b = a.split(",")

    if b[0] =="69":
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
    elif b[0] =="6A":
        data = b[1:len(b)]
        data[-1] = '7E'
        crr_data = data[::-1]

        for i in range(0, len(crr_data)-1, 2):
            a = crr_data[i]+crr_data[i+1]
            value = int(a, 16)*0.0001
            if i<2:
                s1c5.append(value)
            elif i<4:
                s1c6.append(value)
            elif i<6:
                s1c7.append(value)
            else:
                s1c8.append(value)
    if b[0] =="6B":
        data = b[1:len(b)]
        data[-1] = '7E'
        crr_data = data[::-1]

        for i in range(0, len(crr_data)-1, 2):
            a = crr_data[i]+crr_data[i+1]
            value = int(a, 16)*0.0001
            if i<2:
                s1c9.append(value)
            elif i<4:
                s1c10.append(value)
            elif i<6:
                s1c11.append(value)
            else:
                s1c12.append(value)
        
print()


yc1 = np.array(s1c1)
yc2 = np.array(s1c2)
yc3 = np.array(s1c3)
yc4 = np.array(s1c4)
yc5 = np.array(s1c5)
yc6 = np.array(s1c6)
yc7 = np.array(s1c7)
yc8 = np.array(s1c8)
yc9 = np.array(s1c9)
yc10 = np.array(s1c10)
yc11 = np.array(s1c11)
yc12 = np.array(s1c12)

plt.plot(yc1, c='blue', label='C1')
plt.plot(yc2, linestyle = 'dashed', c='black', label='C2')
plt.plot(yc3, linestyle = 'dotted', color = 'brown', label='C3')
plt.plot(yc4, linestyle = 'dashdot', color = 'royalblue', label='C4')
plt.plot(yc5, color = 'aquamarine', label='C5')
plt.plot(yc6, linestyle = 'dashed', color = 'darkslategray', label='C6')
plt.plot(yc7, linestyle = 'dotted', color = 'indigo', label='C7')
plt.plot(yc8, linestyle = 'dashdot', color = 'navy', label='C8')
plt.plot(yc9, color = 'deepskyblue', label='C9')
plt.plot(yc10, linestyle = 'dashed', color = 'darkmagenta', label='C10')
plt.plot(yc11, linestyle = 'dotted', color = 'palegreen', label='C11')
plt.plot(yc12, linestyle = 'dashdot', color = 'teal', label='C12')
plt.legend(bbox_to_anchor =(0.90, 1.15), ncol = 12, loc='upper right')
plt.show()

       
            



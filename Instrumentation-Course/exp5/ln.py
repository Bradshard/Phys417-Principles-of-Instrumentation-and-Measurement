import math
import numpy as np
import matplotlib.pyplot as plt


T = np.linspace(start = 100, stop = 350, num = 50).astype(int)
ohm = np.linspace(start = 400, stop = 1600, num = 50).astype(int)
m = [0.1, 0.025, 0.05, 0.075]
ohm_1 = []
ohm_2 = []
ohm_3 = []
ohm_4 = []


for i in range(len(ohm)):
	ohm_1.append(math.log(ohm[i]*m[0]))
	ohm_2.append(math.log(ohm[i]*m[1]))
	ohm_3.append(math.log(ohm[i]*m[2]))
	ohm_4.append(math.log(ohm[i]*m[3]))


m_1, b_1 = np.polyfit(1000/T, ohm_1, 1)
m_2, b_2 = np.polyfit(1000/T, ohm_2, 1)
m_3, b_3 = np.polyfit(1000/T, ohm_3, 1)
m_4, b_4 = np.polyfit(1000/T, ohm_4, 1)




plt.plot(1000/T, m_1*(1000/T) + b_1)
plt.plot(1000/T, m_2*(1000/T) + b_2)
plt.plot(1000/T, m_3*(1000/T) + b_3)
plt.plot(1000/T, m_4*(1000/T) + b_4)
plt.plot(1000/T, ohm_1, "o",label = "x = 0")
plt.plot(1000/T, ohm_2, "*",label = "x = 0.025")
plt.plot(1000/T, ohm_3, ">",label = "x = 0.05")
plt.plot(1000/T, ohm_4, "1",label = "x = 0.075")
plt.legend()
plt.text(2.8,2.1,"slope is: ")
plt.text(3.7,2.1,b_1)
plt.xlabel('1000/T(K^-1)')
plt.ylabel('ln_rho(omega.m)')
plt.title("omega.m vs 1000/T")


plt.show()

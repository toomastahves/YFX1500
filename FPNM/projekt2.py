import matplotlib.pyplot as plt
import scipy.integrate as ode
import numpy as np

g = 9.814
q = 10**-3
m = 10**-6
h = 5
B = [0.1, 0, 0]
y0 = [0, h, 0, 0, 0, 0]

def func(y, t):
    yp = np.zeros_like(y)
    yp[0] = y[3]
    yp[1] = y[4]
    yp[2] = y[5]
    yp[3] = q / m * (y[4]*B[2] - y[5]*B[1])
    yp[4] = q / m * (y[5]*B[0] - y[3]*B[2]) - g
    yp[5] = q / m * (y[3]*B[1] - y[4]*B[0])
    return yp

time = np.arange(0, 1, 0.001)
res = ode.odeint(func, y0, time)
x, y, z, vx, vy, vz = np.transpose(res)

ekin = 0.5 * m * (vx**2 + vy**2 + vz**2)
epot = m * g * y
etot = np.around(ekin + epot, 10)

plt.figure(figsize=(8,5))
p1 = plt.subplot()
p1.set_title('Trajektoor YZ-tasandil')
p1.set_xlabel('z (m)')
p1.set_ylabel('y (m)')
p1.plot(z, y, color='tab:blue')
p1.grid()

fig, ax1 = plt.subplots()
ax1.set_xlabel('Aeg (s)')
lns1 = ax1.plot(time, ekin*10**8, color='tab:red', label='E-kin (10^-8 J)')
ax1.tick_params(axis='y', labelcolor='tab:red')

ax2 = ax1.twinx()
lns2 = ax2.plot(time, epot*10**8, color='tab:blue', label='E-pot (10^-8 J)')
ax2.tick_params(axis='y', labelcolor='tab:blue')

ax3 = ax1.twinx()
lns3 = ax3.plot(time, etot, color='tab:green', label='E-tot (J)')
ax3.tick_params(axis='y', right=False, labelright=False)

lns = lns1 + lns2 + lns3
labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, loc=1)

ax1.grid()
fig.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as ode

k = 5.0
m = 0.1
alpha = 0.1
omega02 = k / m
beta = alpha / (2 * m)

def func(y, t):
    yp = np.zeros_like(y)
    yp[0] = y[1]
    yp[1] = -2 * beta * y[1] - omega02 * y[0]
    return yp

y0 = [0.1, 0.1]
time = np.arange(0, 10, 0.001)
res = ode.odeint(func, y0, time)

kin = 0.5 * m * res[:,1]**2
pot = 0.5 * k * res[:,0]**2
tot = kin + pot

too = 0
x = y0[0]
korr = list()
for i in range(0, 10000):
    too = too - alpha * res[i,1] * (res[i,0] - x)
    x = res[i,0]
    korr.append(tot[i] - too)


fig = plt.figure(figsize=(10, 10))
p1 = plt.subplot(221)
p1.set_xlabel('t')
p1.set_ylabel('x')
p1.plot(time, res[:,0], color='red', label='x')
p1.grid(color='black')

p2 = plt.subplot(222)
p2.set_xlabel('t')
p2.set_ylabel('v')
p2.plot(time, res[:,1], color='blue', label='v')
p2.grid(color='black')

p3 = plt.subplot(223)
p3.set_xlabel('t')
p3.set_ylabel('E')
p3.plot(time, kin, color='red', label='kin')
p3.plot(time, pot, color='blue', label='pot')
p3.plot(time, tot, color='black', label='tot')
p3.plot(time, korr, color='green', label='korr')
p3.grid(color='black')

plt.show()

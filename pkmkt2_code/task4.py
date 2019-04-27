from task3 import get_velocity_Euler
from sympy import symbols, diff
import numpy as np

x1, x2, x3 = symbols('x1 x2 x3')

def get_euler_dt(eq1, eq2, eq3):
    v1, v2, v3 = get_velocity_Euler(eq1, eq2, eq3)
    vkl = [
        [diff(v1, x1), diff(v1, x2), diff(v1, x3)],
        [diff(v2, x1), diff(v2, x2), diff(v2, x3)],
        [diff(v3, x1), diff(v3, x2), diff(v3, x3)]
    ]
    return vkl

def get_euler_velocity_matrix(eq1, eq2, eq3):
    vkl = get_euler_dt(eq1, eq2, eq3)
    dkl = 0.5*(vkl + np.transpose(vkl))
    return dkl

#from testdata import eq1, eq2, eq3
#print(get_euler_dt(eq1, eq2, eq3))
#print(get_euler_velocity_matrix(eq1, eq2, eq3))

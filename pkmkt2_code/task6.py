from sympy import symbols, diff, N, Matrix
import numpy as np
from task4 import get_euler_dt

X1, X2, X3 = symbols('X1 X2 X3')

def get_vorticity_tensor(eq1, eq2, eq3):
    vkl = get_euler_dt(eq1, eq2, eq3)
    wkl = 0.5*(vkl - np.transpose(vkl))
    return N(Matrix(wkl), 2)

def get_vorticity_components(eq1, eq2, eq3):
    wkl = get_vorticity_tensor(eq1, eq2, eq3) # Tuple, indexes from 0 to 8
    w1 = wkl[7] - wkl[5]
    w2 = wkl[6] - wkl[2]
    w3 = wkl[3] - wkl[1]
    return [w1, w2, w3]

#from testdata import eq1, eq2, eq3
#print(get_vorticity_tensor(eq1, eq2, eq3))
#print(get_vorticity_components(eq1, eq2, eq3))

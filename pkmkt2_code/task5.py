from task4 import get_euler_velocity_matrix
from sympy import symbols, diff
import numpy as np

X1, X2, X3, t = symbols('X1 X2 X3 t')

def get_lagrange_dt(eq1, eq2, eq3):
    xkK = [
        [diff(eq1, X1), diff(eq1, X2), diff(eq1, X3)],
        [diff(eq2, X1), diff(eq2, X2), diff(eq2, X3)],
        [diff(eq3, X1), diff(eq3, X2), diff(eq3, X3)]
    ]
    return xkK

def get_lagrange_velocity_matrix(eq1, eq2, eq3):
    xkK = get_lagrange_dt(eq1, eq2, eq3)
    dkl = get_euler_velocity_matrix(eq1, eq2, eq3)
    EKL = dkl.dot(xkK).dot(np.transpose(xkK))
    return EKL

#from testdata import eq1, eq2, eq3
#print(get_lagrange_dt(eq1, eq2, eq3))
#print(get_lagrange_velocity_matrix(eq1, eq2, eq3))

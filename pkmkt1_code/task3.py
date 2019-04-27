from sympy import diff
from task2 import get_displaced_points
from task1 import get_inverse
import numpy as np
from cube import vertices
from sympy import symbols
from math import sqrt

x1, x2, x3, X1, X2, X3 = symbols('x1 x2 x3 X1 X2 X3')

# Deformation gradients
def get_deformgrad_X_Kk(eq1, eq2, eq3):
    inverse = get_inverse(eq1, eq2, eq3)
    X_Kk = [
        [diff(inverse[X1], x1), diff(inverse[X1], x2), diff(inverse[X1], x3)],
        [diff(inverse[X2], x1), diff(inverse[X2], x2), diff(inverse[X2], x3)],
        [diff(inverse[X3], x1), diff(inverse[X3], x2), diff(inverse[X3], x3)]
    ]
    return X_Kk

def get_deformgrad_x_kK(eq1, eq2, eq3):
    x_kK = [
        [diff(eq1, X1), diff(eq1, X2), diff(eq1, X3)],
        [diff(eq2, X1), diff(eq2, X2), diff(eq2, X3)],
        [diff(eq3, X1), diff(eq3, X2), diff(eq3, X3)],
    ]
    return x_kK

# Calculate ds^2
def get_ds2(eq1, eq2, eq3):
    xkK = get_deformgrad_x_kK(eq1, eq2, eq3)
    xkKT = np.transpose(xkK)
    mat = np.dot(xkKT, xkK)
    ds2 = mat[0][0] + mat[1][1] + mat[2][2] + 2*mat[0][1] + 2*mat[0][2] + 2*mat[1][2]
    return ds2

# Testing
#from testdata import eq1, eq2, eq3
#print(get_deformgrad_X_Kk(eq1, eq2, eq3))
#print(get_deformgrad_x_kK(eq1, eq2, eq3))
#print(get_ds2(eq1, eq2, eq3))


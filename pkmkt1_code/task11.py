from task6 import get_green_dt, get_cauchy_dt
from sympy import Matrix
import numpy as np

def get_green_invariants(eq1, eq2, eq3):
    CKL = get_green_dt(eq1, eq2, eq3)
    a = Matrix(CKL)
    P, D = a.diagonalize()
    D = np.array(D)
    Ic = D[0][0] + D[1][1] + D[2][2]
    IIc = D[0][0]*D[1][1] + D[1][1]*D[2][2] + D[2][2]*D[0][0]
    IIIc = D[0][0]*D[1][1]*D[2][2]
    return [Ic, IIc, IIIc]

def get_cauchy_invariants(eq1, eq2, eq3):
    CKL = get_cauchy_dt(eq1, eq2, eq3)
    a = Matrix(CKL)
    P, D = a.diagonalize()
    D = np.array(D)
    Ic = 1/D[0][0] + 1/D[1][1] + 1/D[2][2]
    IIc = 1/(D[0][0]*D[1][1]) + 1/(D[1][1]*D[2][2]) + 1/(D[2][2]*D[0][0])
    IIIc = 1/(D[0][0]*D[1][1]*D[2][2])
    return [Ic, IIc, IIIc]

# Testing
#from testdata import eq1, eq2, eq3
#print(get_green_invariants(eq1, eq2, eq3))
#print(get_cauchy_invariants(eq1, eq2, eq3))

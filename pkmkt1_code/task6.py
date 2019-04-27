import numpy as np
from sympy import symbols
from task3 import get_deformgrad_X_Kk, get_deformgrad_x_kK

# Cachy deformation tensor
def get_cauchy_dt_wrong(eq1, eq2, eq3):
    X_Kk = get_deformgrad_X_Kk(eq1, eq2, eq3)
    ckl = np.dot(X_Kk, np.transpose(X_Kk))
    return ckl

# Green deformation tensor
def get_green_dt_wrong(eq1, eq2, eq3):
    x_kK = get_deformgrad_x_kK(eq1, eq2, eq3)
    CKL = np.dot(x_kK, np.transpose(x_kK))
    return CKL

# Lagrange deformation tensor
def get_lagrange_dt(eq1, eq2, eq3):
    EKL = 0.5 * (get_green_dt(eq1, eq2, eq3) - np.identity(3))
    #print('Lagrange DT: {0}'.format(simplify(EKL)))
    return EKL

# Euler deformation tensor
def get_euler_dt(eq1, eq2, eq3):
    ekl = 0.5 * (np.identity(3) - get_cauchy_dt(eq1, eq2, eq3))
    #print('Euler DT: {0}'.format(simplify(ekl)))
    return ekl

def get_cauchy_dt(eq1, eq2, eq3):
    mat = get_deformgrad_X_Kk(eq1, eq2, eq3)

    c11 = mat[0][0]**2 + mat[1][0]**2 + mat[2][0]**2
    c22 = mat[0][1]**2 + mat[1][1]**2 + mat[2][1]**2
    c33 = mat[0][2]**2 + mat[1][2]**2 + mat[2][2]**2
    c12 = c21 = mat[0][0]*mat[0][1] + mat[1][0]*mat[1][1] + mat[2][0]*mat[2][1]
    c23 = c32 = mat[0][1]*mat[0][2] + mat[1][1]*mat[1][2] + mat[2][1]*mat[2][2]
    c13 = c31 = mat[0][0]*mat[0][2] + mat[1][0]*mat[1][2] + mat[2][0]*mat[2][2]

    return [[c11, c12, c13], [c21, c22, c23], [c31, c32, c33]]

def get_green_dt(eq1, eq2, eq3):
    mat = get_deformgrad_x_kK(eq1, eq2, eq3)
    
    c11 = mat[0][0]**2 + mat[1][0]**2 + mat[2][0]**2
    c22 = mat[0][1]**2 + mat[1][1]**2 + mat[2][1]**2
    c33 = mat[0][2]**2 + mat[1][2]**2 + mat[2][2]**2
    c12 = c21 = mat[0][0]*mat[0][1] + mat[1][0]*mat[1][1] + mat[2][0]*mat[2][1]
    c23 = c32 = mat[0][1]*mat[0][2] + mat[1][1]*mat[1][2] + mat[2][1]*mat[2][2]
    c13 = c31 = mat[0][0]*mat[0][2] + mat[1][0]*mat[1][2] + mat[2][0]*mat[2][2]

    return [[c11, c12, c13], [c21, c22, c23], [c31, c32, c33]]


# Testing
from testdata import eq1, eq2, eq3
#print(get_cauchy_dt(eq1, eq2, eq3))
print(get_green_dt(eq1, eq2, eq3))
print(get_green_dt_wrong(eq1, eq2, eq3))
#print(get_lagrange_dt(eq1, eq2, eq3))
#print(get_euler_dt(eq1, eq2, eq3))

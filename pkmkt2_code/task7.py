from sympy import symbols, diff, simplify, Matrix, N
import numpy as np
from task5 import get_lagrange_dt
from task1 import get_inverse

X1, X2, X3, x1, x2, x3, t = symbols('X1 X2 X3 x1 x2 x3 t')

def get_xKk(eq1, eq2, eq3):
    inv = get_inverse(eq1, eq2, eq3)
    t1 = np.pi / 4
    xKk = [
        [diff(inv[X1], x1).subs({t: t1}), diff(inv[X1], x2).subs({t: t1}), diff(inv[X1], x3).subs({t: t1})],
        [diff(inv[X2], x1).subs({t: t1}), diff(inv[X2], x2).subs({t: t1}), diff(inv[X2], x3).subs({t: t1})],
        [diff(inv[X3], x1).subs({t: t1}), diff(inv[X3], x2).subs({t: t1}), diff(inv[X3], x3).subs({t: t1})]
    ]
    #xKk = np.around(np.array(xKk).astype(float), decimals = 3)
    return np.array(xKk)

def get_xkK(eq1, eq2, eq3):
    t1 = np.pi / 4
    xkK = [
        [diff(eq1, X1).subs({t: t1}), diff(eq1, X2).subs({t: t1}), diff(eq1, X3).subs({t: t1})],
        [diff(eq2, X1).subs({t: t1}), diff(eq2, X2).subs({t: t1}), diff(eq2, X3).subs({t: t1})],
        [diff(eq3, X1).subs({t: t1}), diff(eq3, X2).subs({t: t1}), diff(eq3, X3).subs({t: t1})]
    ]
    #xkK = np.around(np.array(xkK).astype(float), decimals = 3)
    return np.array(xkK)

def get_jacobian(eq1, eq2, eq3):
    xkK = get_xkK(eq1, eq2, eq3)
    det = Matrix(xkK).det()
    return det

def get_first_piola_kirchoff(eq1, eq2, eq3):
    jac = get_jacobian(eq1, eq2, eq3)
    xKk = get_xKk(eq1, eq2, eq3)
    tkl = [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
    TKl = np.array(xKk).dot(tkl).dot(jac)
    return N(Matrix(TKl), 4)

def get_second_piola_kirchoff(eq1, eq2, eq3):
    TKl = get_first_piola_kirchoff(eq1, eq2, eq3)
    xLl = np.transpose(get_xKk(eq1, eq2, eq3))
    TKL = np.array(TKl).dot(xLl).astype(float)
    TKL = np.around(TKL, decimals = 3)
    return N(Matrix(TKL), 4)

#from testdata import eq1, eq2, eq3
#print(get_xKk(eq1, eq2, eq3))
#print(get_xkK(eq1, eq2, eq3))
#print(get_jacobian(eq1, eq2, eq3))
#print(get_first_piola_kirchoff(eq1, eq2, eq3))
#print(get_second_piola_kirchoff(eq1, eq2, eq3))

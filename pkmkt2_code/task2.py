from task1 import get_Lagrange_descr
from sympy import symbols, diff

x1, x2, x3, t = symbols('x1 x2 x3 t')

def get_velocity_Lagrange(eq1, eq2, eq3):
    U1, U2, U3 = get_Lagrange_descr(eq1, eq2, eq3)
    V1 = diff(U1, t)
    V2 = diff(U2, t)
    V3 = diff(U3, t)
    return [V1, V2, V3]

def get_acceleration_Lagrange(eq1, eq2, eq3):
    V1, V2, V3 = get_velocity_Lagrange(eq1, eq2, eq3)
    A1 = diff(V1, t)
    A2 = diff(V2, t)
    A3 = diff(V3, t)
    return [A1, A2, A3]

#from testdata import eq1, eq2, eq3
#print(get_velocity_Lagrange(eq1, eq2, eq3))
#print(get_acceleration_Lagrange(eq1, eq2, eq3))

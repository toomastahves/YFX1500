from sympy import symbols, diff, solve, Eq
from task1 import get_Euler_descr

x1, x2, x3, t, v1, v2, v3 = symbols('x1 x2 x3 t v1 v2 v3')

def get_velocity_Euler(eq1, eq2, eq3):
    u1, u2, u3 = get_Euler_descr(eq1, eq2, eq3)
    v1_ = diff(u1, t) + diff(u1, x1)*v1 + diff(u1, x2)*v2 + diff(u1, x3)*v3
    v2_ = diff(u2, t) + diff(u2, x1)*v1 + diff(u2, x2)*v2 + diff(u2, x3)*v3
    v3_ = diff(u3, t) + diff(u3, x1)*v1 + diff(u3, x2)*v2 + diff(u3, x3)*v3
    sol = solve([Eq(v1_,v1), Eq(v2_,v2), Eq(v3_,v3)], [v1, v2, v3])
    return [sol[v1], sol[v2], sol[v3]]

def get_acceleration_Euler(eq1, eq2, eq3):
    v1, v2, v3 = get_velocity_Euler(eq1, eq2, eq3)
    a1 = diff(v1, t) + diff(v1, x1)*v1 + diff(v1, x2)*v2 + diff(v1, x3)*v3
    a2 = diff(v2, t) + diff(v2, x1)*v1 + diff(v2, x2)*v2 + diff(v2, x3)*v3
    a3 = diff(v3, t) + diff(v3, x1)*v1 + diff(v3, x2)*v2 + diff(v3, x3)*v3
    return [a1, a2, a3]

#from testdata import eq1, eq2, eq3
#print(get_velocity_Euler(eq1, eq2, eq3))
#print(get_acceleration_Euler(eq1, eq2, eq3))

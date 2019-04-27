from sympy import symbols, simplify, solve, Eq

X1, X2, X3, x1, x2, x3 = symbols('X1 X2 X3 x1 x2 x3')

def get_inverse(eq1, eq2, eq3):
    inverse = solve([Eq(x1, eq1), Eq(x2, eq2), Eq(x3, eq3)], [X1, X2, X3])
    return inverse

def get_Euler_descr(eq1, eq2, eq3):
    inv = get_inverse(eq1, eq2, eq3)
    u1 = simplify(x1 - inv[X1])
    u2 = simplify(x2 - inv[X2])
    u3 = simplify(x3 - inv[X3])
    return [u1, u2, u3]

def get_Lagrange_descr(eq1, eq2, eq3):
    U1 = simplify(eq1 - X1)
    U2 = simplify(eq2 - X2)
    U3 = simplify(eq3 - X3)
    return [U1, U2, U3]

#from testdata import eq1, eq2, eq3
#print(get_inverse(eq1, eq2, eq3))
#print(get_Euler_descr(eq1, eq2, eq3))
#print(get_Lagrange_descr(eq1, eq2, eq3))

from sympy import solve, simplify, Eq, symbols

x1, x2, x3, X1, X2, X3 = symbols('x1 x2 x3 X1 X2 X3')

def get_inverse(eq1, eq2, eq3):
    inverse = solve([Eq(x1, eq1), Eq(x2, eq2), Eq(x3, eq3)], [X1, X2, X3])
    return inverse

def get_Lagrange(eq1, eq2, eq3):
    U1 = simplify(eq1 - X1)
    U2 = simplify(eq2 - X2)
    U3 = simplify(eq3 - X3)
    U = [U1, U2, U3]
    return U

def get_Euler(inverse):
    u1 = simplify(x1 - inverse[X1])
    u2 = simplify(x2 - inverse[X2])
    u3 = simplify(x3 - inverse[X3])
    u = [u1, u2, u3]
    return u

# Testing
#from testdata import eq1, eq2, eq3
#inverse = get_inverse(eq1, eq2, eq3)
#print(get_Lagrange(eq1, eq2, eq3))
#print(get_Euler(inverse))

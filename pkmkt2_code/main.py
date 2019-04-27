from pdf import createlatex
from sympy import sin, cos, symbols, cosh, sinh

X1, X2, X3, x1, x2, x3, t = symbols('X1 X2 X3 x1 x2 x3 t')

nr11 = [
    11,
    -X1*cos(t) + 5*X2*sin(t),
    -X1*sin(t) - 5*X2*cos(t),
    X3
]
nr12 = [
    12,
    X1*sin(t) + X2*cos(t),
    -X1*cos(t) + X2*sin(t),
    X3
]
nr13 = [
    13,
    6*X1*sin(t) + 4*X2*cos(t),
    -6*X1*cos(t) + 4*X2*sin(t),
    X3
]
nr15 = [
    15,
    -3*X1*cos(t) - 4*X2*sin(t),
    3*X1*sin(t) - 4*X2*cos(t),
    X3
]
nr16 = [
    16,
    -4*X1*cos(t) - 3*X2*sin(t),
    4*X1*sin(t) - 3*X2*cos(t),
    X3
]
nr17 = [
    17,
    -6*X1*cos(t) + 2*X2*sin(t),
    -6*X1*sin(t) - 2*X2*cos(t),
    X3
]
nr18 = [
    18,
    -2*X1*cos(t) + 6*X2*sin(t),
    -2*X1*sin(t) - 6*X2*cos(t),
    X3
]
nr22 = [
    22,
    -X1*cos(t) + 2*X2*sin(t),
    -X1*sin(t) - 2*X2*cos(t),
    X3
]

if __name__ == "__main__":

    ver = nr15
    
    nr = ver[0]
    eq1 = ver[1]
    eq2 = ver[2]
    eq3 = ver[3]

    createlatex(eq1, eq2, eq3, filename='KT2 nr{0}'.format(nr))

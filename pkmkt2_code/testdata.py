from sympy import sin, cos, symbols

# Test data
X1, X2, X3, x1, x2, x3, t = symbols('X1 X2 X3 x1 x2 x3 t')
eq1 = X1*sin(t) + X2*cos(t)
eq2 = -X1*cos(t) + X2*sin(t)
eq3 = X3

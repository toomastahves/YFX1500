from sympy import symbols
from pdf import createpdf
from latex import createlatex

if __name__ == "__main__":

    X1, X2, X3 = symbols('X1 X2 X3')
    
    nr = 18
    eq1 = 2/3*X1+2/3*X2
    eq2 = -X1+X2
    eq3 = X3

    createlatex(eq1, eq2, eq3, filename='variant{0}_latex'.format(nr))

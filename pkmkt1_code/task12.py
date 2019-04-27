from task11 import get_green_invariants, get_cauchy_invariants

def is_isohoric(eq1, eq2, eq3):
    Ic, IIc, IIIc = get_green_invariants(eq1, eq2, eq3)
    Ic2, IIc2, IIIc2 = get_cauchy_invariants(eq1, eq2, eq3)
    return (IIIc == 1) & (IIIc2 == 1)

# Testing
#from testdata import eq1, eq2, eq3
#print('Is ishoric? {0}'.format(is_isohoric(eq1, eq2, eq3)))

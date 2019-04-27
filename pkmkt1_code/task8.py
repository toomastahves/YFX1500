from task7 import get_green_eig
from math import sqrt

def get_stretch_extension(eq1, eq2, eq3):
    values, vectors = get_green_eig(eq1, eq2, eq3)
    L1 = sqrt(values[0])
    L2 = sqrt(values[1])
    L3 = sqrt(values[2])
    stretch = [L1, L2, L3]
    E1 = L1 - 1
    E2 = L2 - 1
    E3 = L3 - 1
    extension = [E1, E2, E3]
    #print('Λ1 = {0} , Λ2 = {1}, Λ3 = {2}'.format(L1, L2, L3))
    #print('E1 = {0} , E2 = {1}, E3 = {2}'.format(E1, E2, E3))
    return stretch, extension

# Testing
#from testdata import eq1, eq2, eq3
#print(get_stretch_extension(eq1, eq2, eq3))

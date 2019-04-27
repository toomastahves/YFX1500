import numpy as np
from task7 import get_green_eig, get_cauchy_eig

def get_rotation_tensor(eq1, eq2, eq3):
    values1, vectors1 = get_cauchy_eig(eq1, eq2, eq3)
    values2, vectors2 = get_green_eig(eq1, eq2, eq3)

    nka = np.concatenate(vectors1)
    nka = nka.reshape((3,3))
    nka = np.transpose(nka)

    NaK = np.concatenate(vectors2)
    NaK = NaK.reshape((3,3))

    RkK = np.dot(nka, NaK)

    return RkK

# Testing
#from testdata import eq1, eq2, eq3
#print(get_rotation_tensor(eq1, eq2, eq3))

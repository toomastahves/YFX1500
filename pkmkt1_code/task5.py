import numpy as np
from task2 import get_displaced_points
from cube import vertices

# Get changed angle.
# Example: Getting changed angle between X1 and X2: get_angle_gamma('X1', 'X2', eq1, eq2, eq3)
def get_angle_gamma(x1, x2, eq1, eq2, eq3):
    i1 = get_index(x1)
    i2 = get_index(x2)
    displaced = get_displaced_points(eq1, eq2, eq3, vertices)
    v1 = np.array(displaced[i1], dtype=float)
    v2 = np.array(displaced[i2], dtype=float)
    cos_fi = np.dot(v1, v2) / (np.linalg.norm(v1)*np.linalg.norm(v2))
    fi = np.arccos(cos_fi)
    angle = 90 - np.rad2deg(fi)
    return angle

# Angle mapping to cube point indexes
def get_index(x):
    if(x == 'X1'): return 3 # 'OA'
    elif(x == 'X2'): return 1 # 'OC'
    elif(x == 'X3'): return 4 # 'OD'

# Testing
#from testdata import eq1, eq2, eq3
#print(get_angle_gamma('X1', 'X2', eq1, eq2, eq3))

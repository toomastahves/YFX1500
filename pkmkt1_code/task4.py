import numpy as np
from math import sqrt
from sympy import Matrix
from task2 import get_displaced_points
from cube import vertices
from task6 import get_green_dt

# Naive way to calculate coefficent. Find way to use tensors.
def get_coefficent(eq1, eq2, eq3, i1, i2):
    displaced = get_displaced_points(eq1, eq2, eq3, vertices)
    before = calc_distance(vertices[i1], vertices[i2])**2
    after = calc_distance(displaced[i1], displaced[i2])**2
    lam2 = after / before
    return lam2

# Distance between two points
def calc_distance(p1, p2):
    dist = sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2)
    return dist

# Get single angle in degrees
def get_angle(i, displaced):
    v1 = np.array(displaced[i], dtype=float)
    v2 = np.array(vertices[i], dtype=float)
    cos_fi = np.dot(v1, v2) / (np.linalg.norm(v1)*np.linalg.norm(v2))
    fi = np.arccos(cos_fi)
    angle = np.rad2deg(fi)
    return angle

# Calculate rotation angles
def get_angles(eq1, eq2, eq3):
    displaced = get_displaced_points(eq1, eq2, eq3, vertices)
    angles = []
    for i in range(1,8):
        angle = get_angle(i, displaced)
        angles.append(['0{0}'.format(get_name(i)), np.around(angle, 3)])
    return angles

# Calculate coefficents
def get_lambdas(eq1, eq2, eq3):
    coefficents = []
    for i in range(1, 8):
        c = np.around(sqrt(get_coefficent(eq1, eq2, eq3, 0, i)), 3)
        coefficents.append(['0{0}'.format(get_name(i)), c])
    return coefficents

# Just letter names of the points
def get_name(i):
    if(i==0): return '0'
    elif(i==1): return 'C'
    elif(i==2): return 'B'
    elif(i==3): return 'A'
    elif(i==4): return 'D'
    elif(i==5): return 'G'
    elif(i==6): return 'F'
    elif(i==7): return 'E'

# Testing
#from testdata import eq1, eq2, eq3
#print(get_lambdas(eq1, eq2, eq3))
#print(get_angles(eq1, eq2, eq3))

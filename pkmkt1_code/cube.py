from sympy import symbols

dX = symbols('dX')
dX = 1

# Points forming cube
vertices = [
    [0,0,0], # vertices[0] = '0'
    [0,dX,0], # vertices[1] = 'C'
    [dX,dX,0], # vertices[2] = 'B'
    [dX,0,0], # vertices[3] = 'A'
    [0,0,dX], # vertices[4] = 'D'
    [0,dX,dX], # vertices[5] = 'G'
    [dX,dX,dX], # vertices[6] = 'F'
    [dX,0,dX]  # vertices[7] = 'E'
]

# Lines connecting points. Built using indexes of vertices array
edges = [
    [0,1], # edges[0] = '0C'
    [1,2], # edges[1] = 'CB'
    [2,3], # edges[2] = 'BA'
    [3,0], # edges[3] = 'A0'
    [0,4], # edges[4] = '0D'
    [1,5], # edges[5] = 'CG'
    [2,6], # edges[6] = 'BF'
    [3,7], # edges[7] = 'AE'
    [4,5], # edges[8] = 'DG'
    [5,6], # edges[9] = 'GF'
    [6,7], # edges[10] = 'FE'
    [7,4]  # edges[11] = 'ED'
]

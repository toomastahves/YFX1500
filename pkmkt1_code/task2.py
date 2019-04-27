import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from mpl_toolkits.mplot3d import Axes3D
from cube import vertices, edges, dX
from task1 import get_Lagrange
from sympy import symbols

x1, x2, x3, X1, X2, X3, C = symbols('x1 x2 x3 X1 X2 X3 C')

# Visualization
def plot(eq1, eq2, eq3):
    fig = plt.figure()
    fig.set_size_inches(6, 6)
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    ax = fig.add_subplot(111, projection = '3d')
    #ax._axis3don = False
    ax.view_init(azim = 45)

    # Needed to make x,y,z axes same length (default view is distorted)
    lim = 1
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_zlim(-lim, lim)

    # Label axes
    ax.set_xlabel('X1')
    ax.set_ylabel('X2')
    ax.set_zlabel('X3')

    # Lines and arrow heads
    ax.quiver(0, 0, 0, 1, 0, 0, color='black', length=1.75, arrow_length_ratio = 0.05)
    ax.quiver(0, 0, 0, 0, 1, 0, color='black', length=1.75, arrow_length_ratio = 0.05)
    ax.quiver(0, 0, 0, 0, 0, 1, color='black', length=1.75, arrow_length_ratio = 0.05)
    
    # Text near arrow heads
    ax.text(1.75,0,0.1, s='X1', fontsize=14, color='black')
    ax.text(0,1.75,0, s='X2', fontsize=14, color='black')
    ax.text(0,0,1.75, s='X3', fontsize=14, color='black')
    
    # Get points with displacement and draw lines
    displaced = get_displaced_points(eq1, eq2, eq3, vertices)
    draw_lines(vertices, 'black', 'o')
    draw_lines(displaced, 'red', 'o')

    # Annotate points
    get_annotations(displaced, ax)
    

def get_annotations(p, ax):
    ax.text(0,0,0, s='0', fontsize=14)
    ax.text(dX,0,0, s='A', fontsize=14)
    ax.text(dX,dX,0, s='B', fontsize=14)
    ax.text(0,dX,0, s='C', fontsize=14)
    ax.text(0,0,dX, s='D', fontsize=14)
    ax.text(dX,0,dX, s='E', fontsize=14)
    ax.text(dX,dX,dX, s='F', fontsize=14)
    ax.text(0,dX,dX, s='G', fontsize=14)
    ax.text(p[0][0],p[0][1],p[0][2], s='0\'', fontsize=14, color='red')
    ax.text(p[1][0],p[1][1],p[1][2], s='C\'', fontsize=14, color='red')
    ax.text(p[2][0],p[2][1],p[2][2], s='B\'', fontsize=14, color='red')
    ax.text(p[3][0],p[3][1],p[3][2], s='A\'', fontsize=14, color='red')
    ax.text(p[4][0],p[4][1],p[4][2], s='D\'', fontsize=14, color='red')
    ax.text(p[5][0],p[5][1],p[5][2], s='G\'', fontsize=14, color='red')
    ax.text(p[6][0],p[6][1],p[6][2], s='F\'', fontsize=14, color='red')
    ax.text(p[7][0],p[7][1],p[7][2], s='E\'', fontsize=14, color='red')

# Draw lines between points
def draw_lines(points, color, marker):
    for e in edges:
        line = [points[e[0]], points[e[1]]]
        lx, ly, lz = np.transpose(line)
        plt.plot(lx, ly, lz, marker = marker, color = color, linewidth=0.5, markersize=3)

# Finds displacement of point p
def get_displacement(eq1, eq2, eq3, p):
    [U1, U2, U3] = get_Lagrange(eq1, eq2, eq3)
    mov_x1 = U1.subs({X1:p[0], X2:p[1], X3:p[2]})
    mov_x2 = U2.subs({X1:p[0], X2:p[1], X3:p[2]})
    mov_x3 = U3.subs({X1:p[0], X2:p[1], X3:p[2]})
    return [mov_x1, mov_x2, mov_x3]

# Finds new point location
def get_new_location(eq1, eq2, eq3, p):
    [U1, U2, U3] = get_displacement(eq1, eq2, eq3, p)
    new_x1 = p[0] + U1
    new_x2 = p[1] + U2
    new_x3 = p[2] + U3
    return [new_x1, new_x2, new_x3]

# Uses two functions above to calculate new location for all points
def get_displaced_points(eq1, eq2, eq3, vertices):
    displaced = []
    for p in vertices:
        new_point = get_new_location(eq1, eq2, eq3, p)
        displaced.append(new_point)
    return displaced

# Opens matplotlib editor
def show(eq1, eq2, eq3):
    plot(eq1, eq2, eq3)
    plt.show()

# Saves image
def create_cube_image(eq1, eq2, eq3):
    plot(eq1, eq2, eq3)
    plt.savefig('img/cube.png')

# Testing
#from testdata import eq1, eq2, eq3
#show(eq1, eq2, eq3)
#create_cube_image(eq1, eq2, eq3)

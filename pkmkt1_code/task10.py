import numpy as np
from sympy import solve, Eq, Matrix, symbols
from task7 import get_green_eig, get_cauchy_eig
from math import cos, sin, sqrt
import matplotlib.pyplot as plt

# Parameter k value
def get_k(eq1, eq2, eq3):
    Ca, directions1 = get_green_eig(eq1, eq2, eq3)
    return sqrt(np.sum(Ca))

# Calculating ellipsoid axes lengths
def get_ellipsoid_axes(t, eq1, eq2, eq3):
    Ca, directions1 = get_green_eig(eq1, eq2, eq3) 
    ca, directions2 = get_cauchy_eig(eq1, eq2, eq3) 
    k = get_k(eq1, eq2, eq3)
    if(t == 'green'): # spatial
        a1 = k / sqrt(Ca[0])
        a2 = k / sqrt(Ca[1])
        a3 = k / sqrt(Ca[2])
        return [a1, a2, a3], directions1
    if(t == 'cauchy'): # material
        a1 = k * sqrt(Ca[0])
        a2 = k * sqrt(Ca[1])
        a3 = k * sqrt(Ca[2])
        return [a1, a2, a3], directions2

# Plot ellipses
def draw_ellipses(lengths, vectors, ax):
    a, b, c = lengths
    a_vec, b_vec, c_vec = vectors
    angles = np.arange(-np.pi-np.pi/30, np.pi+np.pi/30, np.pi/30)

    x, y, z = get_ellipse_points(a, a_vec, b, b_vec, angles)
    ax.plot(x, y, z, color = 'green')

    x, y, z = get_ellipse_points(a, a_vec, c, c_vec, angles)
    ax.plot(x, y, z, color = 'blue')
    
    x, y, z = get_ellipse_points(b, b_vec, c, c_vec, angles)
    ax.plot(x, y, z, color = 'purple')

# Calculate points on ellipse
def get_ellipse_points(len1, vec1, len2, vec2, angles):
    x = []
    y = []
    z = []
    for u in angles:
        x.append( len1*vec1[0]*sin(u) + len2*vec2[0]*cos(u) )
        y.append( len1*vec1[1]*sin(u) + len2*vec2[1]*cos(u) ) 
        z.append( len1*vec1[2]*sin(u) + len2*vec2[2]*cos(u) )
    return x, y, z

# Drawing direction vectors
def draw_vectors(values, vectors, color, ax):
    for i, v in enumerate(vectors):
        line = [-4*v, 4*v]
        lx, ly, lz = np.transpose(line)
        ax.quiver(0, 0, 0, lx, ly, lz, color=color, arrow_length_ratio = 0.02)

def plot(t, eq1, eq2, eq3):
    fig = plt.figure()
    fig.set_size_inches(10, 10)
    ax = fig.add_subplot(111, projection = '3d')
    ax.view_init(azim = 60)

    # Needed to make x,y,z axes same length (default view is distorted)
    lim = 2
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_zlim(-lim, lim)

    # Label axes
    ax.set_xlabel('X1')
    ax.set_ylabel('X2')
    ax.set_zlabel('X3')
    
    # Lines and arrow heads
    ax.quiver(0, 0, 0, 1, 0, 0, color='black', length=3.5, arrow_length_ratio = 0.05, linewidth=1)
    ax.quiver(0, 0, 0, 0, 1, 0, color='black', length=3.5, arrow_length_ratio = 0.05, linewidth=1)
    ax.quiver(0, 0, 0, 0, 0, 1, color='black', length=3.5, arrow_length_ratio = 0.05, linewidth=1)   

    # Annotate points
    get_annotations(ax)

    # Drawing ellipses
    if(t == 'cauchy'):
        lengths, vectors = get_ellipsoid_axes('cauchy', eq1, eq2, eq3)
        draw_ellipses(lengths, vectors, ax)
        # Drawing direction vectors
        values, vectors = get_cauchy_eig(eq1, eq2, eq3)
        draw_vectors(values, vectors, 'red', ax)

    if(t == 'green'):
        lengths, vectors = get_ellipsoid_axes('green', eq1, eq2, eq3)
        draw_ellipses(lengths, vectors, ax)
        # Drawing direction vectors
        values, vectors = get_green_eig(eq1, eq2, eq3)
        draw_vectors(values, vectors, 'red', ax)


def get_annotations(ax):
    ax.text(0,0,0, s='0', fontsize=14)
    ax.text(4,0,0, s='X1', fontsize=14)
    ax.text(0,3.5,0, s='X2', fontsize=14)
    ax.text(0,0,3, s='X3', fontsize=14)

# Opens matplotlib editor
def show(t, eq1, eq2, eq3):
    plot(t, eq1, eq2, eq3)
    plt.show()

# Saves image
def create_ellipse_image(t, eq1, eq2, eq3):
    plot(t, eq1, eq2, eq3)
    plt.savefig('img/ellipses_{0}.png'.format(t))


# Testing
#from testdata import eq1, eq2, eq3
#show('cauchy', eq1, eq2, eq3)
#show('green', eq1, eq2, eq3)
#create_ellipse_image('cauchy', eq1, eq2, eq3)
#create_ellipse_image('green', eq1, eq2, eq3)

import numpy as np
from sympy import solve, Matrix, symbols
from task6 import get_green_dt, get_cauchy_dt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

C = symbols('C')

def get_green_eig(eq1, eq2, eq3):
    CKL = get_green_dt(eq1, eq2, eq3)
    m = CKL - C * np.identity(3)
    m = Matrix(m)
    result = m.eigenvects()
    values = []
    vectors = []
    for r in result:
        sol = solve(r[0], C)
        vec = np.array(r[2]).astype(np.float64).flatten()
        vec = vec / np.linalg.norm(vec)
        values.append(sol[0])
        vectors.append(vec)
    # C1 > C2 > C3
    ret = np.transpose([values, vectors])
    ret = ret[np.argsort(-ret[:,0])] # sort desc
    values, vectors = np.transpose(ret)

    vectors = np.concatenate(vectors)
    vectors = vectors.reshape((3,3))

    return values, vectors

def get_cauchy_eig(eq1, eq2, eq3):
    ckl = get_cauchy_dt(eq1, eq2, eq3)
    m = ckl - C * np.identity(3)
    m = Matrix(m)
    result = m.eigenvects()
    values = []
    vectors = []
    for r in result:
        sol = solve(r[0], C)
        vec = np.array(r[2]).astype(np.float64).flatten()
        vec = vec / np.linalg.norm(vec)
        values.append(sol[0])
        vectors.append(vec)
    # c1 < c2 < c3
    ret = np.transpose([values, vectors])
    ret = ret[np.argsort(ret[:,0])] # sort asc
    values, vectors = np.transpose(ret)

    vectors = np.concatenate(vectors)
    vectors = vectors.reshape((3,3))

    return values, vectors

def draw_vectors(values, vectors, color, ax):
    for i, v in enumerate(vectors):
        line = [[0,0,0], v]
        lx, ly, lz = np.transpose(line)
        ax.quiver(0, 0, 0, lx, ly, lz, color = color, arrow_length_ratio = 0.1)

# Visualization
def plot(eq1, eq2, eq3):
    fig = plt.figure()
    fig.set_size_inches(7, 7)
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
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
    ax.quiver(0, 0, 0, 1, 0, 0, color='black', length=2.5, arrow_length_ratio = 0.05, linewidth=0.5)
    ax.quiver(0, 0, 0, 0, 1, 0, color='black', length=2.5, arrow_length_ratio = 0.05, linewidth=0.5)
    ax.quiver(0, 0, 0, 0, 0, 1, color='black', length=2.5, arrow_length_ratio = 0.05, linewidth=0.5)

    # Draw vectors
    values1, vectors1 = get_green_eig(eq1, eq2, eq3)
    draw_vectors(values1, vectors1, 'green', ax)
    values2, vectors2 = get_cauchy_eig(eq1, eq2, eq3)
    draw_vectors(values2, vectors2, 'blue', ax)

    # Annotate points
    get_annotations(vectors1, vectors2, ax)


def get_annotations(vectors1, vectors2, ax):
    ax.text(0,0,0, s='0', fontsize=14)
    ax.text(2.5,0,0.1, s='X1', fontsize=14)
    ax.text(0,2.5,0, s='X2', fontsize=14)
    ax.text(0,0,2.5, s='X3', fontsize=14)

    N11, N12, N13 = vectors1[0]
    N21, N22, N23 = vectors1[1]
    N31, N32, N33 = vectors1[2]
    ax.text(N11, N12, N13, s='N1', fontsize=14, color='green')
    ax.text(N21, N22, N23, s='N2', fontsize=14, color='green')
    ax.text(N31, N32, N33+0.1, s='N3', fontsize=14, color='green')

    N11, N12, N13 = vectors2[0]
    N21, N22, N23 = vectors2[1]
    N31, N32, N33 = vectors2[2]
    ax.text(N11,N12,N13, s='n1', fontsize=14, color='blue')
    ax.text(N21, N22-0.4, N23, s='n2', fontsize=14, color='blue')
    ax.text(N31, N32, N33+0.1, s='n3', fontsize=14, color='blue')

# Opens matplotlib editor
def show(eq1, eq2, eq3):
    plot(eq1, eq2, eq3)
    plt.show()

# Saves image
def create_eigs_image(eq1, eq2, eq3):
    plot(eq1, eq2, eq3)
    plt.savefig('img/eigs.png')

# Testing
#from testdata import eq1, eq2, eq3
#show(eq1, eq2, eq3)
#create_eigs_image(eq1, eq2, eq3)
#val1, vec1 = get_green_eig(eq1, eq2, eq3)
#val2, vec2 = get_cauchy_eig(eq1, eq2, eq3)

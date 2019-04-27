import time
import numpy as np
from sympy import symbols, preorder_traversal, Float
from pylatex import Document, Section, Subsection, Math, Matrix, NoEscape, Figure, Command

from task1 import get_inverse, get_Lagrange, get_Euler
from task2 import create_cube_image
from task3 import get_ds2, get_deformgrad_X_Kk, get_deformgrad_x_kK
from task4 import get_angles, get_lambdas
from task5 import get_angle_gamma
from task6 import get_cauchy_dt, get_green_dt, get_lagrange_dt, get_euler_dt
from task7 import get_green_eig, get_cauchy_eig, create_eigs_image
from task8 import get_stretch_extension
from task9 import get_rotation_tensor
from task10 import get_k, get_ellipsoid_axes, create_ellipse_image
from task11 import get_green_invariants, get_cauchy_invariants
from task12 import is_isohoric

# Rounding inside sympy equations
def round_eq(eq):
    for a in preorder_traversal(eq):
        if isinstance(a, Float):
            eq = eq.subs(a, round(a, 3))
    return eq

def createlatex(eq1, eq2, eq3, filename):
    X1, X2, X3 = symbols('X1 X2 X3')
    
    # Async process, generate images
    create_cube_image(eq1, eq2, eq3)
    create_eigs_image(eq1, eq2, eq3)
    create_ellipse_image('cauchy', eq1, eq2, eq3)
    create_ellipse_image('green', eq1, eq2, eq3)
    time.sleep(2)

    # Preface   
    geometry_options = {"tmargin": "1cm", "lmargin": "1cm"}
    doc = Document(geometry_options = geometry_options)
    doc.append('Initial equations')
    doc.append(Math(data=['x1', '=', round_eq(eq1)]))
    doc.append(Math(data=['x2', '=', round_eq(eq2)]))
    doc.append(Math(data=['x3', '=', round_eq(eq3)]))
    doc.append(NoEscape(r'\hrule'))

    # Create all answers
    inverse = get_inverse(eq1, eq2, eq3)
    lagrange = get_Lagrange(eq1, eq2, eq3)
    euler = get_Euler(inverse)
    ds2 = get_ds2(eq1, eq2, eq3)
    lambdas = get_lambdas(eq1, eq2, eq3)
    angles = get_angles(eq1, eq2, eq3)
    gamma = get_angle_gamma('X1', 'X2', eq1, eq2, eq3)
    XKk = np.around(np.array(get_deformgrad_X_Kk(eq1, eq2, eq3), dtype=np.float32), 3)
    xkK = np.around(np.array(get_deformgrad_x_kK(eq1, eq2, eq3), dtype=np.float32), 3)
    cauchy_dt = np.around(np.array(get_cauchy_dt(eq1, eq2, eq3), dtype=np.float32), 3)
    green_dt = np.around(np.array(get_green_dt(eq1, eq2, eq3), dtype=np.float32), 3)
    lagrange_dt = np.around(np.array(get_lagrange_dt(eq1, eq2, eq3), dtype=np.float32), 3)
    euler_dt = np.around(np.array(get_euler_dt(eq1, eq2, eq3), dtype=np.float32), 3)
    eig_val1, eig_vec1 = get_green_eig(eq1, eq2, eq3)
    eig_val1 = np.around(np.array([eig_val1], dtype=np.float32).T, 3)
    eig_vec1 = np.around(np.array(eig_vec1, dtype=np.float32), 3)
    eig_val2, eig_vec2 = get_cauchy_eig(eq1, eq2, eq3)
    eig_val2 = np.around(np.array([eig_val2], dtype=np.float32).T, 3)
    eig_vec2 = np.around(np.array(eig_vec2, dtype=np.float32), 3)
    stretch, extension = get_stretch_extension(eq1, eq2, eq3)
    stretch = np.around(np.array([stretch], dtype=np.float32).T, 3)
    extension = np.around(np.array([extension], dtype=np.float32).T, 3)
    RkK = np.around(np.array(get_rotation_tensor(eq1, eq2, eq3), dtype=np.float32), 3)
    k_val = np.around(float(get_k(eq1, eq2, eq3)), 3)
    axes1, direction1 = get_ellipsoid_axes('cauchy', eq1, eq2, eq3)
    ellipse_axes_cauchy = np.around(np.array([axes1], dtype=np.float32).T, 3)
    axes2, direction2 = get_ellipsoid_axes('green', eq1, eq2, eq3)
    ellipse_axes_green = np.around(np.array([axes2], dtype=np.float32).T, 3)
    inv_green = np.around(np.array(get_green_invariants(eq1, eq2, eq3), dtype=np.float32).T, 3)
    inv_cauchy = np.around(np.array(get_cauchy_invariants(eq1, eq2, eq3), dtype=np.float32).T, 3)
    isohoric = 'Yes' if is_isohoric(eq1, eq2, eq3) == True else 'No'

    # 1 Task
    section = Section('Task')
    # 1.1 Inverse equation
    subsection = Subsection('Inverse equation')
    subsection.append(Math(data=['X1', '=', round_eq(inverse[X1])]))
    subsection.append(Math(data=['X2', '=', round_eq(inverse[X2])]))
    subsection.append(Math(data=['X3', '=', round_eq(inverse[X3])]))
    section.append(subsection)
    # 1.2 Lagrangian description
    subsection = Subsection('Lagrangian description')
    subsection.append(Math(data=['U1', '=', round_eq(lagrange[0])]))
    subsection.append(Math(data=['U2', '=', round_eq(lagrange[1])]))
    subsection.append(Math(data=['U3', '=', round_eq(lagrange[2])]))
    section.append(subsection)
    # 1.3 Eulerian description
    subsection = Subsection('Eulerian description')
    subsection.append(Math(data=['u1', '=', round_eq(euler[0])]))
    subsection.append(Math(data=['u2', '=', round_eq(euler[1])]))
    subsection.append(Math(data=['u3', '=', round_eq(euler[2])]))
    section.append(subsection)
    section.append(NoEscape(r'\hrule'))
    doc.append(section)

    # 2 Task
    section = Section('Task')
    subsection = Subsection('Original and displaced cube')
    section.append(subsection)
    cube = Figure(position='h!')
    cube.add_image('img/cube.png', width='250px')
    section.append(cube)
    section.append(NoEscape(r'\hrule'))
    doc.append(section)

    # 3 Task
    section = Section('Task')
    subsection = Subsection('Diagonal square length after change')
    subsection.append(Math(data=['ds2', '=', np.around(float(ds2), 3)]))
    section.append(subsection)
    section.append(NoEscape(r'\hrule'))
    doc.append(section)

    # 4 Task
    section = Section('Task')
    subsection = Subsection('Stretch ratios')
    for l in lambdas: subsection.append(Math(data=[l[0], '=', l[1]]))
    section.append(subsection)
    subsection = Subsection('Rotation angles')
    for l in angles: subsection.append(Math(data=[l[0], '=', l[1]]))
    section.append(subsection)
    section.append(NoEscape(r'\hrule'))
    doc.append(section)

    # 5 Task
    section = Section('Task')
    subsection = Subsection('Gamma between X1 and X2')
    subsection.append(Math(data=['Gamma', '=', np.round(float(gamma),3)]))
    section.append(subsection)
    section.append(NoEscape(r'\hrule'))
    doc.append(section)

    # 6 Task
    section = Section('Task')
    subsection = Subsection('Deformation gradients')
    subsection.append(Math(data=['XKk', '=', Matrix(XKk)]))
    subsection.append(Math(data=['xkK', '=', Matrix(xkK)]))
    section.append(subsection)
    subsection = Subsection('Green tensor')
    subsection.append(Math(data=['CKL', '=', Matrix(green_dt)]))
    section.append(subsection)
    subsection = Subsection('Cauchy tensor')
    subsection.append(Math(data=['ckl', '=', Matrix(cauchy_dt)]))
    section.append(subsection)
    subsection = Subsection('Lagrange tensor')
    subsection.append(Math(data=['EKL', '=', Matrix(lagrange_dt)]))
    section.append(subsection)
    subsection = Subsection('Euler tensor')
    subsection.append(Math(data=['ekl', '=', Matrix(euler_dt)]))
    section.append(subsection)
    section.append(NoEscape(r'\hrule'))
    doc.append(section)

    # 7 Task
    section = Section('Task')
    subsection = Subsection('Green eigenvalues')
    subsection.append(Math(data=['C', '=', Matrix(eig_val1)]))
    section.append(subsection)
    subsection = Subsection('Green eigenvectors (vectors in rows)')
    subsection.append(Math(data=['N', '=', Matrix(eig_vec1)]))
    section.append(subsection)
    subsection = Subsection('Cauchy eigenvalues')
    subsection.append(Math(data=['c', '=', Matrix(eig_val2)]))
    section.append(subsection)
    subsection = Subsection('Cauchy eigenvectors (vectors in rows)')
    subsection.append(Math(data=['n', '=', Matrix(eig_vec2)]))
    section.append(subsection)
    doc.append(section)
    doc.append(Command('newpage'))
    subsection = Subsection('Eigenvectors plot')
    eigs = Figure(position='h!')
    eigs.add_image('img/eigs.png', width='250px')
    subsection.append(eigs)
    subsection.append(NoEscape(r'\hrule'))
    doc.append(subsection)

    # 8 Task
    section = Section('Task')
    subsection = Subsection('Stretch')
    subsection.append(Math(data=['L', '=', Matrix(stretch)]))
    section.append(subsection)
    subsection = Subsection('Extension')
    subsection.append(Math(data=['E', '=', Matrix(extension)]))
    section.append(subsection)
    section.append(NoEscape(r'\hrule'))
    doc.append(section)

    # 9 Task
    section = Section('Task')
    subsection = Subsection('Rotation matrix')
    subsection.append(Math(data=['R', '=', Matrix(RkK)]))
    section.append(subsection)
    section.append(NoEscape(r'\hrule'))
    doc.append(section)
    doc.append(Command('newpage'))

    # 10 Task
    section = Section('Task')
    subsection = Subsection('Parameter k')
    subsection.append(Math(data=['k', '=', k_val]))
    section.append(subsection)
    subsection = Subsection('Ellipse axes length (Cauchy direction)')
    subsection.append(Math(data=['a1', '=', Matrix(ellipse_axes_cauchy)]))
    section.append(subsection)
    subsection = Subsection('Ellipse axes length (Green direction)')
    subsection.append(Math(data=['a2', '=', Matrix(ellipse_axes_green)]))
    section.append(subsection)
    subsection = Subsection('Ellipse plot (Cauchy left, Green right)')
    ellipses = Figure(position='h!')
    ellipses.add_image('img/ellipses_cauchy.png', width='250px')
    ellipses.add_image('img/ellipses_green.png', width='250px')
    subsection.append(ellipses)    
    section.append(subsection)
    section.append(NoEscape(r'\hrule'))
    doc.append(section)
    doc.append(Command('newpage'))

    # 11 Task
    section = Section('Task')
    subsection = Subsection('Green tensor invairants')
    subsection.append(Math(data=['IC', '=', inv_green[0]]))
    subsection.append(Math(data=['IIC', '=', inv_green[1]]))
    subsection.append(Math(data=['IIIC', '=', inv_green[2]]))
    section.append(subsection)
    subsection = Subsection('Cauchy tensor invairants')
    subsection.append(Math(data=['Ic', '=', inv_cauchy[0]]))
    subsection.append(Math(data=['IIc', '=', inv_cauchy[1]]))
    subsection.append(Math(data=['IIIc', '=', inv_cauchy[2]]))
    section.append(subsection)
    section.append(NoEscape(r'\hrule'))
    doc.append(section)

    # 12 Task
    section = Section('Task')
    subsection = Subsection('Is deformatsion isohoric?')
    subsection.append(isohoric)
    section.append(subsection)
    doc.append(section)
    
    doc.generate_pdf(filename, clean_tex = True, compiler = 'pdflatex')

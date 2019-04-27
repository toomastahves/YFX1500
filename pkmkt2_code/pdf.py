from pylatex import Document, Section, Subsection, Math, Matrix, NoEscape, Figure, Command
from sympy import symbols
import numpy as np
from task1 import get_inverse, get_Euler_descr, get_Lagrange_descr
from task2 import get_velocity_Lagrange, get_acceleration_Lagrange
from task3 import get_velocity_Euler, get_acceleration_Euler
from task4 import get_euler_velocity_matrix
from task5 import get_lagrange_velocity_matrix
from task6 import get_vorticity_tensor, get_vorticity_components
from task7 import get_first_piola_kirchoff, get_second_piola_kirchoff, get_xKk, get_xkK, get_jacobian

def createlatex(eq1, eq2, eq3, filename):
    X1, X2, X3 = symbols('X1 X2 X3')

    # Create all answers
    inverse = get_inverse(eq1, eq2, eq3)
    euler = get_Euler_descr(eq1, eq2, eq3)
    lagrange = get_Lagrange_descr(eq1, eq2, eq3)
    lagrange_velocity = get_velocity_Lagrange(eq1, eq2, eq3)
    lagrange_acceleration = get_acceleration_Lagrange(eq1, eq2, eq3)
    euler_velocity = get_velocity_Euler(eq1, eq2, eq3)
    euler_acceleration = get_acceleration_Euler(eq1, eq2, eq3)
    euler_velocity_matrix = get_euler_velocity_matrix(eq1, eq2, eq3)
    lagrange_velocity_matrix = get_lagrange_velocity_matrix(eq1, eq2, eq3)
    vorticity_tensor = get_vorticity_tensor(eq1, eq2, eq3)
    vorticity_components = get_vorticity_components(eq1, eq2, eq3)
    first_piola_kirchoff = get_first_piola_kirchoff(eq1, eq2, eq3)
    second_piola_kirchoff = get_second_piola_kirchoff(eq1, eq2, eq3)
    xKk = np.around(np.array(get_xKk(eq1, eq2, eq3)).astype(float), decimals = 3)
    xkK = np.around(np.array(get_xkK(eq1, eq2, eq3)).astype(float), decimals = 3)
    jacobian = np.around(float(get_jacobian(eq1, eq2, eq3)), decimals = 3)

    # Document settings
    geometry_options = {"tmargin": "1cm", "lmargin": "1cm"}
    doc = Document(geometry_options = geometry_options)

    # Initial equations
    section = Section('Initial equations', numbering=False)
    section.append(Math(data=['x1', '=', eq1]))
    section.append(Math(data=['x2', '=', eq2]))
    section.append(Math(data=['x3', '=', eq3]))
    section.append(NoEscape(r'\hrule'))
    doc.append(section)

    # Task 1
    section = Section('Task')
    # 1.1 Inverse equation
    subsection = Subsection('Inverse equation')
    subsection.append(Math(data=['X1', '=', inverse[X1]]))
    subsection.append(Math(data=['X2', '=', inverse[X2]]))
    subsection.append(Math(data=['X3', '=', inverse[X3]]))
    section.append(subsection)
    # 1.2 Euler
    subsection = Subsection('Euler description')
    subsection.append(Math(data=['u1', '=', euler[0]]))
    subsection.append(Math(data=['u2', '=', euler[1]]))
    subsection.append(Math(data=['u3', '=', euler[2]]))
    section.append(subsection)
    # 1.3 Lagrange
    subsection = Subsection('Lagrange description')
    subsection.append(Math(data=['U1', '=', lagrange[0]]))
    subsection.append(Math(data=['U2', '=', lagrange[1]]))
    subsection.append(Math(data=['U3', '=', lagrange[2]]))
    section.append(subsection)
    doc.append(section)

    # Task 2
    section = Section('Task')
    # 2.1 Lagrange velocity
    subsection = Subsection('Lagrange velocity')
    subsection.append(Math(data=['V1', '=', lagrange_velocity[0]]))
    subsection.append(Math(data=['V2', '=', lagrange_velocity[1]]))
    subsection.append(Math(data=['V3', '=', lagrange_velocity[2]]))
    section.append(subsection)
    # 2.2 Lagrange acceleration
    subsection = Subsection('Lagrange acceleration')
    subsection.append(Math(data=['A1', '=', lagrange_acceleration[0]]))
    subsection.append(Math(data=['A2', '=', lagrange_acceleration[1]]))
    subsection.append(Math(data=['A3', '=', lagrange_acceleration[2]]))
    section.append(subsection)
    doc.append(section)

    # Task 3
    section = Section('Task')
    # 3.1 Euler velocity
    subsection = Subsection('Euler velocity')
    subsection.append(Math(data=['v1', '=', euler_velocity[0]]))
    subsection.append(Math(data=['v2', '=', euler_velocity[1]]))
    subsection.append(Math(data=['v3', '=', euler_velocity[2]]))
    section.append(subsection)
    # 3.2 Euler acceleration
    subsection = Subsection('Euler acceleration')
    subsection.append(Math(data=['a1', '=', euler_acceleration[0]]))
    subsection.append(Math(data=['a2', '=', euler_acceleration[1]]))
    subsection.append(Math(data=['a3', '=', euler_acceleration[2]]))
    section.append(subsection)
    doc.append(section)

    # Task 4
    section = Section('Task')
    section.append(Math(data=['dkl', '=', Matrix(euler_velocity_matrix)]))
    doc.append(section)

    # Task 5
    section = Section('Task')
    section.append(Math(data=['EKL', '=', Matrix(lagrange_velocity_matrix)]))
    doc.append(section)

    # Task 6
    section = Section('Task')
    # 6.1
    subsection = Subsection('Vorticity matrix')
    subsection.append(Math(data=['wkl', '=', Matrix(vorticity_tensor)]))
    section.append(subsection)
    # 6.2
    subsection = Subsection('Vorticity components')
    subsection.append(Math(data=['w1', '=', vorticity_components[0]]))
    subsection.append(Math(data=['w2', '=', vorticity_components[1]]))
    subsection.append(Math(data=['w3', '=', vorticity_components[2]]))
    section.append(subsection)
    doc.append(section)

    # Task 7
    section = Section('Task')
    section.append(Math(data=['xKk', '=', Matrix(xKk)]))
    section.append(Math(data=['xkK', '=', Matrix(xkK)]))
    section.append(Math(data=['j', '=', jacobian]))
    # 7.1
    subsection = Subsection('First Piola-Kirchoff tensor')
    subsection.append(Math(data=['TKl', '=', Matrix(first_piola_kirchoff)]))
    section.append(subsection)
    # 7.2
    subsection = Subsection('Second Piola-Kirchoff tensor')
    subsection.append(Math(data=['TKL', '=', Matrix(second_piola_kirchoff)]))
    section.append(subsection)
    doc.append(section)

    doc.generate_pdf(filename, clean_tex = True, compiler = 'pdflatex')

#from testdata import eq1, eq2, eq3
#createlatex(eq1, eq2, eq3, 'test')

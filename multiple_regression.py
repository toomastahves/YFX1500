# -*- coding: utf-8 -*-

from Vectors import dot
from Gradient import minimize_stochastic
import random
from linear_regression import total_sum_of_squares

def predict(x_i, beta):
    return dot(x_i, beta)

def error(x_i, y_i, beta):
    return y_i - predict(x_i, beta)

def squared_error(x_i, y_i, beta):
    return error(x_i, y_i, beta) ** 2

def squared_error_gradient(x_i, y_i, beta):
    return [-2 * x_ij * error(x_i, y_i, beta) for x_ij in x_i]

def estimate_beta(x, y):
    beta_initial = [random.random() for x_i in x[0]]
    return minimize_stochastic(squared_error, squared_error_gradient, x, y, beta_initial, 0.001)

random.seed(0)
x = [[1,2,3,4],[1,2,3,4]]
minutes = [2,4,6,8,10]
beta = estimate_beta(x, minutes)

def multiple_r_squared(x, y, beta):
    sum_of_squared_errors = sum(error(x_i, y_i, beta) ** 2 for x_i, y_i in zip(x, y))
    return 1.0 - sum_of_squared_errors /total_sum_of_squares(y)


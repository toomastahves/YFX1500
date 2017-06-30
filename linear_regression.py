# -*- coding: utf-8 -*-
from Statistics import correlation, standard_deviation, mean, de_mean
import matplotlib.pyplot as plt
import random
from Gradient import minimize_stochastic

def predict(alpha, beta, x_i):
    return beta * x_i + alpha

def error(alpha, beta, x_i, y_i):
    return y_i - predict(alpha, beta, x_i)

def sum_of_squared_errors(alpha,  beta, x, y):
    return sum(error(alpha, beta, x_i, y_i) ** 2 for x_i, y_i in zip(x, y))

def least_squares_fit(x, y):
    beta = correlation(x, y) * standard_deviation(y) / standard_deviation(x)
    alpha = mean(y) - beta * mean(x)
    return alpha, beta

friends = [1,2,3,4,5,6,6,8,9,10]
minutes = [2,4,7,8,10,12,14,15,18,21]
alpha, beta = least_squares_fit(friends, minutes)

# Plot
plt.scatter(friends, minutes)
print(alpha, beta)
values = []
elements = []
for i in range(0, 11):
    values.append(i)
    elements.append(beta * i + alpha)

plt.plot(values, elements)


def total_sum_of_squares(y):
    return sum(v ** 2 for v in de_mean(y))

def r_squared(alpha, beta, x, y):
    return 1.0 - (sum_of_squared_errors(alpha, beta, x, y) / total_sum_of_squares(y))

res = r_squared(alpha, beta, friends, minutes)

# Gradient
def squared_error(x_i, y_i, theta):
    alpha, beta = theta
    return error(alpha, beta, x_i, y_i) ** 2

def squared_error_gradient(x_i, y_i, theta):
    alpha, beta = theta
    return [ -2 * error(alpha, beta, x_i, y_i), # alpha partial derivative
            -2 * error(alpha, beta, x_i, y_i) * x_i] # beta partial derivative

random.seed(0)
theta = [random.random(), random.random()]
alpha, beta = minimize_stochastic(squared_error, squared_error_gradient, friends, minutes, theta, 0.0001)
print(alpha, beta)

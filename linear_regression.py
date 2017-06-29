# -*- coding: utf-8 -*-
from Statistics import correlation, standard_deviation, mean

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

friends = [1,2,3,4,5,6,7,8,9,10]
minutes = [2,4,6,8,10,12,14,16,18,20]
alpha, beta = least_squares_fit(friends, minutes)

print(alpha, beta)

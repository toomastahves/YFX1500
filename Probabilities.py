# -*- coding: utf-8 -*-
import math 
import Distribution

# n - number of tries
# p - hypothesis if true 0 < p < 1
# mu - mean
# sigma - standard deviation
def normal_approximation_to_binomial(n, p):
    mu = p * n
    sigma = math.sqrt(p * (1-p) * n)
    return mu, sigma
# Example
# mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)
# mu_0 = 500 and sigma_0 = 15.8

normal_probability_below = Distribution.normal_cdf

def normal_probability_above(lo, mu=0, sigma=1):
    return 1 - Distribution.normal_cdf(lo, mu, sigma)

def normal_probability_between(lo, hi, mu=0, sigma=1):
    return Distribution.normal_cdf(hi, mu, sigma) - Distribution.normal_cdf(lo, mu, sigma)

def normal_probability_outside(lo, hi, mu=0, sigma=1):
    return 1 - normal_probability_between(lo, hi, mu, sigma)

def normal_upper_bound(probability, mu=0, sigma=1):
    return Distribution.inverse_normal_cdf(probability, mu, sigma)

def normal_lower_bound(probability, mu=0, sigma=1):
    return Distribution.inverse_normal_cdf(1 - probability, mu, sigma)

# 0 < probability < 1
def normal_two_sided_bounds(probability, mu=0, sigma=1):
    tail_probability = (1 - probability) / 2
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)
    lower_bound = normal_upper_bound(tail_probability, mu, sigma)
    return lower_bound, upper_bound
# Example
# lower, upper = normal_two_sided_bounds(0.95, 500, 15.8)
# lower = 469, upper = 530

def two_sided_p_value(x, mu=0, sigma=1):
    if x >= mu:
        return 2 * normal_probability_above(x, mu, sigma)
    else:
        return 2 * normal_probability_below(x, mu, sigma)
# Example
# print(two_sided_p_value(529.5, 500, 15.8)) 0.062


# -*- coding: utf-8 -*-
import math

# https://en.wikipedia.org/wiki/Normal_distribution
# Probability density function
def normal_pdf(x, mu = 0, sigma = 1):
    return (1/math.sqrt(2*math.pi*sigma**2))*math.exp(-(x-mu)**2/(2*sigma**2))
# Cumulative distribution function
def normal_cdf(x, mu = 0, sigma = 1):
    return 0.5*(1+math.erf((x-mu)/(sigma*math.sqrt(2))))

# https://en.wikipedia.org/wiki/Binary_search_algorithm
def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    """find approximate inverse using binary search"""
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)
    
    low_z, low_p = -10.0, 0 # normal_cdf(-10) is (very close to) 0
    hi_z, hi_p = 10.0, 1 # normal_cdf(10) is (very close to) 1
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2 # consider the midpoint
        mid_p = normal_cdf(mid_z) # and the cdf's value there
        if mid_p < p:
            # midpoint is still too low, search above it
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
            # midpoint is still too high, search below it
            hi_z, hi_p = mid_z, mid_p
        else:
            break
    return mid_z

#Examples
#from matplotlib import pyplot as plt
#xs = [x / 10.0 for x in range(-50, 51)]
#plt.plot(xs, [normal_pdf(x, mu = 0, sigma = math.sqrt(0.2)) for x in xs])
#plt.plot(xs, [normal_cdf(x, mu = 0, sigma = 1) for x in xs])
#plt.plot(xs, [inverse_normal_cdf(x, mu = 0, sigma = 1) for x in xs])

# -*- coding: utf-8 -*-
import math

def vector_add(v, w):
    return [v_i + w_i
            for v_i, w_i in zip(v, w)]

def vector_subtract(v, w):
    return [v_i - w_i
            for v_i, w_i in zip(v, w)]
    
def vector_sum(vectors):
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result, vector)
    return result

def scalar_multiply(c, v):
    return [c * v_i 
            for v_i in v]

def vector_mean(vectors):
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

def dot(v, w):
    a = (v_i * w_i for v_i, w_i in zip(v, w))
    d = 0
    for i in a:
        d+=i
    return d
    
def sum_of_squares(v):
    return dot(v, v)

def magnitude(v):
    return math.sqrt(sum_of_squares(v))

def squared_distance(v, w):
    return sum_of_squares(vector_subtract(v, w))

def distance(v, w):
    return magnitude(vector_subtract(v, w))


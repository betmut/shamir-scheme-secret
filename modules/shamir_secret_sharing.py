from random import randint 
from math import gcd

# create galois field order p (a field with a set {0,1,2,3,...,p-1} 
# under mod p operation)
PRIME = 71

# define k-1 degree Polynomial
def create_polynomial(secret, minimal):
    return [secret] + [randint(0,PRIME) for _ in range(minimal-1)]

# create shares
def create_shares(shares, polynomial):
    threshold = len(polynomial)
    # if k > n, raise an error
    if threshold > shares:
        raise ValueError("Pool secret would be irrecoverable.")
    points = []
    for x in range(1, shares + 1):
        value = sum(coefficient * x**power 
                    for power, coefficient in enumerate(polynomial))
        points.append((x, value % PRIME))
    return points

# modular inverse of a
# there exist a integer x such that a.x = 1 (mod m)
# the x uniquely exist if and only if gcd(a, m) = 1
# fermat little theorem case if gcd(a.m) = 1: a^(p-1) = a.a^(p-2) = 1 (mod p)

# this modular inverse implementation is not good since exponentiation is 
# computationally slow as the number bigger.
def _modular_inverse(number, divisor):
    if gcd(number, divisor) != 1:
        raise ValueError("the inverse is not found")
    return pow(number, divisor-2) % divisor

def _basis_polynomial(x, order, points):
    if order >= len(points):
        raise ValueError("order is exceeded the length of points")
    prod = 1
    denom = 1
    for i in range(len(points)):
        if i == order:
            continue
        else:
            prod *= (x-points[i])
            denom *= (points[order] - points[i])
    denom_mod_inverse = _modular_inverse(denom, PRIME)
    return (prod * denom_mod_inverse) % PRIME

def lagrange_interpolation(x, sample_points, sample_shares):
    interpolation_sum = sum( share * _basis_polynomial(x, i, sample_points) 
                            for i, share in enumerate(sample_shares)) % PRIME
    return interpolation_sum

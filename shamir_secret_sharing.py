from random import sample, randint 

# create galois field order p (a field with a set {0,1,2,3,...,p-1} 
# under mod p operation)
PRIME = 71

# define k-1 degree Polynomial
def create_polynomial(secret, minimal):
    return [secret % PRIME] + [randint(0,PRIME) for _ in range(minimal-1)]

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

# interpolate k share 
def interpolate_shares(picked_shares):
    return interpolated_polys_coeffs 



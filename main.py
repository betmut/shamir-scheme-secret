from random import sample, randint 

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

def main():
    secret = 62
    n = 20
    threshold = 4

    polynomial = create_polynomial(secret, threshold)
    shares = create_shares(n, polynomial)
    pick_random_shares = sample(shares, k = 5)

    print(polynomial)
    print(shares)
    print(pick_random_shares)

if __name__ == "__main__":
    main()

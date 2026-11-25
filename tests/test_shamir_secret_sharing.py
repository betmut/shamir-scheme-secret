import modules.shamir_secret_sharing as shamir
from random import sample 

#check degree of polynomial
def test_polynomial_degree():
    assert len(shamir.create_polynomial(63, 10)) == 10
    assert len(shamir.create_polynomial(123, 15)) == 15

def test_secret_recovery():
    secret = 63
    n = 50
    threshold = 10

    # Create Polynomial
    polynomial = shamir.create_polynomial(secret, threshold)

    # Create n shares
    point_of_shares = shamir.create_shares(n, polynomial)

    # Pick sample of share points 
    picked_point_of_shares = sample(point_of_shares, k = 20)
    picked_points, picked_shares = zip(*picked_point_of_shares)

    # interpolation
    recovered_secret = shamir.lagrange_interpolation(0, picked_points, picked_shares)
    assert recovered_secret == secret



import pytest
import modules.shamir_secret_sharing as shamir
from random import sample 

#check degree of polynomial
@pytest.mark.parametrize(
        "secret, threshold, expected_number_of_coefficients",
        [
            (63, 10, 10),
            (63, 10, 10),
            (123, 15, 15)
        ]
)
def test_polynomial_coefficients(secret, threshold, expected_number_of_coefficients):
    assert len(shamir.create_polynomial(secret, threshold)) == expected_number_of_coefficients


@pytest.mark.parametrize(
        "secret, n, threshold, picked_shares",
        [
            (63, 50, 10, 12),
            (63, 70, 7, 8),
            (123, 75, 7, 10)
        ]
)
def test_secret_recovery(secret, n, threshold, picked_shares):
    # Create Polynomial
    polynomial = shamir.create_polynomial(secret, threshold)

    # Create n shares
    point_of_shares = shamir.create_shares(n, polynomial)

    # Pick sample of share points 
    picked_point_of_shares = sample(point_of_shares, k = picked_shares)
    picked_points, picked_shares = zip(*picked_point_of_shares)

    # interpolation
    recovered_secret = shamir.lagrange_interpolation(0, picked_points, picked_shares)
    assert recovered_secret == secret



from random import sample 
import modules.shamir_secret_sharing as shamir 

def main():
    secret = 63
    n = 23
    threshold = 5

    # Create Polynomial
    polynomial = shamir.create_polynomial(secret, threshold)

    # Create n shares
    point_of_shares = shamir.create_shares(n, polynomial)

    # Pick sample of share points 
    picked_point_of_shares = sample(point_of_shares, k = 10)
    picked_points, picked_shares = zip(*picked_point_of_shares)

    # interpolation
    recovered_secret = shamir.lagrange_interpolation(0, picked_points, picked_shares)

    # display the result
    print(f"Polynomial: {polynomial}")
    print(f"Point of shares: {point_of_shares}")
    print(f"Picked point of shares: {picked_point_of_shares}")
    print(f"Secret after interpolation: {recovered_secret}")

if __name__ == "__main__":
    main()

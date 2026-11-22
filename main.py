from random import sample 
from shamir_secret_sharing import create_polynomial, create_shares

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

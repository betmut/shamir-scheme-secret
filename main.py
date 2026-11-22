from random import sample 
import modules.shamir_secret_sharing as shamir 

def main():
    secret = 62
    n = 20
    threshold = 4

    polynomial = shamir.create_polynomial(secret, threshold)
    shares = shamir.create_shares(n, polynomial)
    pick_random_shares = sample(shares, k = 5)

    print(polynomial)
    print(shares)
    print(pick_random_shares)

if __name__ == "__main__":
    main()

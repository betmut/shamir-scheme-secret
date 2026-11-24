def _isPrime(number):
    if number == 2:
        return True
    if number < 2:
        return False
    if number % 2 == 0:
        return False

    i = 3
    while i * i <= number:
        if number % i == 0:
            return False
        i += 2
    return True

def primes_up_to(n):
    return [x for x in range(n+1) if _isPrime(x)]

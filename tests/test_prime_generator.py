from modules.prime_generator import primes_up_to, _isPrime

def test_check_prime():
    assert _isPrime(2) == True
    assert _isPrime(3) == True
    assert _isPrime(4) == False
    assert _isPrime(12910) == False


def test_pick_max_prime():
    assert max(primes_up_to(6)) == 5
    assert max(primes_up_to(30)) == 29


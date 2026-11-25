import pytest
from modules.prime_generator import primes_up_to, _isPrime

@pytest.mark.parametrize("n", [2, 3, 5, 97])
def test_is_prime(n):
    assert _isPrime(n)

@pytest.mark.parametrize("n", [-5, 0, 1, 4, 9, 25, 100])
def test_is_not_prime(n):
    assert not _isPrime(n)

@pytest.mark.parametrize(
    "limit, expected",
    [
        (-1, []),
        (0, []),
        (1, []),
        (2, [2]),
        (3, [2, 3]),        # prime limit is included
        (4, [2, 3]),        # composite limit isn't included
        (10, [2, 3, 5, 7])  # test bigger case
    ],
)
def test_primes_up_to_edge_cases(limit, expected):
    assert primes_up_to(limit) == expected

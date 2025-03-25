from src.practice_2025_03_24.is_prime import is_prime

def test_primes():
    assert is_prime(2)
    assert is_prime(17)

def test_non_primes():
    assert not is_prime(1)
    assert not is_prime(4)
    assert not is_prime(0)

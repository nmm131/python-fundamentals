def get_first_20_prime_numbers():
    non_primes = set(not_a_prime_number for step in range(2, 8) for not_a_prime_number in range(step * 2, 20, step))
    first_20_prime_numbers = [prime_number for prime_number in range(2, 20) if prime_number not in non_primes]
    return first_20_prime_numbers

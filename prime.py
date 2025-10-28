def is_prime(n: int) -> bool:
    """Return True if n is prime (works for n >= 0)."""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def sieve(limit: int) -> list:
    """Return list of primes <= limit using Sieve of Eratosthenes."""
    if limit < 2:
        return []
    sieve = bytearray(b'\x01') * (limit + 1)
    sieve[0:2] = b'\x00\x00'
    p = 2
    while p * p <= limit:
        if sieve[p]:
            step = p
            start = p * p
            sieve[start:limit+1:step] = b'\x00' * ((limit - start)//step + 1)
        p += 1
    return [i for i, is_p in enumerate(sieve) if is_p]

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Prime utilities")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", "-c", type=int, help="Check if number is prime")
    group.add_argument("--upto", "-u", type=int, help="List primes up to N")
    args = parser.parse_args()

    if args.check is not None:
        n = args.check
        print(f"{n} is prime" if is_prime(n) else f"{n} is not prime")
    else:
        primes = sieve(args.upto)
        print(primes)
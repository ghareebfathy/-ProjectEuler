# project 72
def sieves(R: int = 1000000) -> int:
    """
    Return the number of reduced proper fractions with denominator less than limit.
    >>> sieves(8)
    21
    >>> sieves(1000)
    304191
    """

    sieve = [True] * R
    primes = set()
    for n in range(2, R + 1):
        if sieve[n - 1]:
            primes.add(n)  # add numbert primes to convert number to string
            sieve[n * n - 1::n] = [False] * len(range(n * n - 1, R, n))

    phi = [(n) for n in range(R + 1)]

    for p in primes:
        for n in range(p, R + 1, p):
            phi[n] *= 1 - 1 / p

    return int(sum(phi[2:]))


if __name__ == "__main__":
    print(f"{sieves()}")
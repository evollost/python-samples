def CountPrimes(n):
    if n < 3:
        return 0
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in xrange(2, int(n ** 0.5)+1):
        if primes[i]:
            primes[i * i: n: i] = [False] * len(xrange(i * i, n, i))
    return primes.count(True)

print CountPrimes(1000000)

'''
Sieve of Eratosthenes

Time: O(n log log n)
Space: O(n)
'''

def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for multiple in range(p*p, n+1, p):
                is_prime[multiple] = False

    return [i for i in range(2, n+1) if is_prime[i]]



'''
Incremental Prime Generation (Trial Division)

Use when: Generating primes one-by-one, unknown upper bound
Time: O(n√n) (bad for large n)
'''



'''
Segmented Sieve → For N > 10^8 (memory-efficient)
Miller–Rabin → For primality testing, not generation
Wheel Factorization → Constant-factor optimization only
'''


from math import sqrt
from typing import List

from test_framework import generic_test


# TC: O(n^(3/2)), SC: O(n)
# Actual TC and SC should be much better since algorithm often returns false early and most numbers in 0..=n are not stored in the list returned
def trial_division(n: int) -> List[int]:
    primes = []
    for i in range(2, n + 1):
        is_prime = True
        for prime in primes:
            if i % prime == 0:
                is_prime = False
                break
            elif prime >= sqrt(i):
                break
        if is_prime:
            primes.append(i)
    return primes


# TC: O(n*log(log(n))) ,SC: O(n)
# TC could be formulated as follows: O(n/2 + n/3 + n/5 + n/7 + n/11..), which asymptotically tends to n * log(log(n))
def sieve(n: int) -> List[int]:
    primes = []
    is_prime = [False, False] + [True] * (n - 1)
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            j = 2
            while i * j <= n:
                is_prime[j * i] = False
                j += 1
    return primes


# TC: O(n*log(log(n))) ,SC: O(n/2)
# TC, SC are the same as unoptimized sieving above, but faster with less memory footprint
# represent each candidate number p by 2*i +3, where i >= 0 and i < floor((n-3)/2)+1 to only consider odd numbers ranging from 3
# when p is a prime number, sieve out p^2, p^2 * 2*p, p^2 * 4*p  ... as p*k for k < p has already been sieved by previous primes.
# Also note that each step between two sieving is 2 * p, not p, because p is prime and therefore odd number.
# This means p^2 is odd. so p^2 + (2*k+1)*p will result in even number, which cannot be prime (other than 2)
# This also works well with our is_prime list.
# Because is_prime[j] represents 2*j + 3, is_prime[j+k*p] for k=0,1,2,3.. represents (2*j+3)+ 2*(k*p)=p+2*k*p
def optimized_sieve(n: int) -> List[int]:
    if n < 2:
        return []
    primes = [2]
    size = (n - 3) // 2 + 1
    is_prime = [True] * size
    for i in range(size):
        if is_prime[i]:
            p = i * 2 + 3
            primes.append(p)
            for j in range(2 * (i**2) + 6 * i + 3, size, p):
                is_prime[j] = False
    return primes


# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    # return trial_division(n)
    # return sieve(n)
    return optimized_sieve(n)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "prime_sieve.py", "prime_sieve.tsv", generate_primes
        )
    )

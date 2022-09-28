"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes<=0:
        raise ValueError
    list = []
    i = 2
    while len(list) < number_of_primes and i < 1000:
        # for possiblePrime in range(2, 21):
            isPrime = True
            for num in range(2, i):
                if i % num == 0:
                    isPrime = False
                    break
            if isPrime == True:
                list.append(i)
            i = i + 1

    return list

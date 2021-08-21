import copy


def returnNextPrime(lastPrime):
    candidate = lastPrime+1
    divider = 2
    while True:
        while candidate % divider != 0:
            divider += 1
        if candidate == divider:
            return candidate
        else:
            candidate += 1


def returnPrimeListUnderSomeNumber(someNumber):
    if someNumber < 3:
        return [2]
    primes = [2]
    nextPrime = returnNextPrime(primes[-1])
    while nextPrime < someNumber:
        nextPrime = returnNextPrime(primes[-1])
        if nextPrime < someNumber:
            primes.append(copy.deepcopy(nextPrime))
    return primes

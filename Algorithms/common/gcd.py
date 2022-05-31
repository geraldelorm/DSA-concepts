# Naive Solution
def gcd(numerator, denominator): # greatest common divisor
    best = 0
    for x in range(1, numerator + denominator):
        if numerator % x == 0 and denominator % x == 0:
            best = x
    return best

# Time Complexity = O(n)  -- n + m
# Space Complexity = o(1)


# Optimal Solution
def gcd(numerator, denominator): # greatest common divisor -- gcd(a,b) = gcd(b,a')
    if denominator == 0:
        return numerator
    numPrime = numerator % denominator
    return gcd(denominator, numPrime)

print(gcd(357,234))
# Time Complexity = O(logn)
# Space Complexity = o(1)
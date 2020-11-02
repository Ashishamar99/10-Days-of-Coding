# we can import math and use math.factorial(n), but let's use a loop to calculate factorial.
def factorial(n):
    res = 1
    if n > 1:
        for i in range(1, n+1):
            res *= i
    return res

def fetch_trail_zeroes(fact):
    trail_count = 0
    fact = str(fact)
    fact = fact[::-1]
    for char in fact:
        if char == '0': trail_count += 1
        else: break
    return trail_count

if __name__ == '__main__':
    n = int(input('n = '))
    fact = factorial(n)
    trail_count = fetch_trail_zeroes(fact)
    print(trail_count)
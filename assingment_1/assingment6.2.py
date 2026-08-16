def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def add_primes(n):
    sum = 0
    for i in range(2, n + 1):
        if is_prime(i):
            sum += i
    return sum

n = int(input("Enter a number: "))
result = add_primes(n)
print("The sum of all prime numbers from 1 to", n, "is:", result)
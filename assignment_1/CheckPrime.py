a=int(input("Enter number: "))
is_prime = True
if a < 2:
    is_prime = False
else:
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            is_prime = False
            break
if is_prime:
    print(a, "is a prime number")
else:
    print(a, "is not a prime number")
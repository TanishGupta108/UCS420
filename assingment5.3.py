n=int(input("Enter number: "))
sum=0
is_prime = True
for i in range(2, n+1):
    if n < 2:
        is_prime = False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                is_prime = False
            break
            if is_prime:
                sum=sum+i
print("Sum of prime numbers is: ", sum)

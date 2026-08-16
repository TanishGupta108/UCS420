def add_odd_numbers(n):
    total = 0
    for i in range(1, n+1):
        if i % 2 != 0:
            total += i
    return total

n = int(input("Enter a number: "))
result = add_odd_numbers(n)
print("The sum of all odd numbers from 1 to", n, "is:", result)
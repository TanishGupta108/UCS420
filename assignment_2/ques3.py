import random
from collections import Counter

roll_number = input("Enter your roll number: ")

digits = [int(digit) for digit in roll_number]
L = [digit * 10 for digit in digits]

print("\nQ3. RANDOM NUMBERS")

# Use roll number as random seed
random.seed(int(roll_number))

#ques 3 part 1
numbers = [random.randint(100, 900) for _ in range(100)]

print("Generated list of 100 random numbers:")
print(numbers)

# ques 3 part 2
odd_numbers = [x for x in numbers if x % 2 != 0]

print("\nOdd numbers:")
print(odd_numbers)
print("Number of odd numbers:", len(odd_numbers))

# ques 3 part 3
even_numbers = [x for x in numbers if x % 2 == 0]

print("\nEven numbers:")
print(even_numbers)
print("Number of even numbers:", len(even_numbers))

# ques 3 part 4
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


prime_numbers = [x for x in numbers if is_prime(x)]

print("\nPrime numbers:")
print(prime_numbers)
print("Number of prime numbers:", len(prime_numbers))

# ques 3 part 5
frequency = Counter(numbers)

most_frequent_number, frequency_count = frequency.most_common(1)[0]

print("\nMost frequently occurring number:", most_frequent_number)
print("Number of occurrences:", frequency_count)
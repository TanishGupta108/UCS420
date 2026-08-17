roll_number = input("Enter your roll number: ")

digits = [int(digit) for digit in roll_number]
L = [digit * 10 for digit in digits]
print("\nQ4. SET OPERATIONS")

first_8_digits = [int(digit) for digit in roll_number[:8]]

A = {digit * 7 for digit in first_8_digits}
B = {digit * 9 for digit in first_8_digits}

print("Set A:", A)
print("Set B:", B)

# ques 4 part 6
union = A.union(B)
print("\nUnion of A and B:", union)

# ques 4 part 7
intersection = A.intersection(B)
print("Intersection of A and B:", intersection)

# ques 4 part 8
A_minus_B = A.difference(B)
B_minus_A = B.difference(A)

print("A - B:", A_minus_B)
print("B - A:", B_minus_A)

# difference() gives elements present only in the first set.
# symmetric_difference() gives elements present in either set but not in both.

# ques 4 part 9
symmetric_difference = A.symmetric_difference(B)
print("Symmetric difference:", symmetric_difference)

# ques 4 part 10
print("Is A a subset of B?", A.issubset(B))
print("Is B a superset of A?", B.issuperset(A))

# ques 4 part 11
X = int(input("\nEnter a value X to remove from set A: "))

A.discard(X)

print("Set A after discard:", A)

# discard() does not raise an error if the specified value does not exist,
# whereas remove() raises a KeyError.
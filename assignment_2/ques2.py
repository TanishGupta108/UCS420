roll_number = input("Enter your roll number: ")

digits = [int(digit) for digit in roll_number]
L = [digit * 10 for digit in digits]
# First 8 values from L
scores = tuple(L[:8])

print("\nQ2. TUPLE OPERATIONS")
print("Scores tuple:", scores)

# ques 2 part 1
highest = max(scores)
highest_index = scores.index(highest)

# Lowest score and frequency
lowest = min(scores)
lowest_count = scores.count(lowest)

print("Highest score:", highest)
print("Index of highest score:", highest_index)
print("Lowest score:", lowest)
print("Number of times lowest score appears:", lowest_count)

# ques 2 part 2
reversed_scores = list(reversed(scores))
print("Reversed tuple as list:", reversed_scores)

# ques 2 part 3
user_score = int(input("Enter a score to search in tuple: "))

if user_score in scores:
    print("First occurrence index:", scores.index(user_score))
else:
    print("Score is not present in the tuple.")

# ques 2 part 4
print("\nAttempting to modify tuple:")

try:
    scores[0] = 100
except TypeError as e:
    print("Error:", e)
    # Tuples are immutable, so their elements cannot be changed directly.
    # Lists are mutable, so list elements can be changed.

# ques 2 part 5
first_score, second_score, *remaining_scores = scores

print("First score:", first_score)
print("Second score:", second_score)
print("Remaining scores:", remaining_scores)
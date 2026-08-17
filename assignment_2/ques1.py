roll_number = input("Enter your roll number: ")

digits = [int(digit) for digit in roll_number]
L = [digit * 10 for digit in digits]

# ques 1 part 1
print("\nQ1. LIST OPERATIONS")
print("Original list L:", L)

# ques 1 part 2
L.append(100)
print("After append(100):", L)
# append() adds the new element at the end of the list.

L.insert(2, 200)
print("After insert(2, 200):", L)
# insert() adds 200 at index 2 and shifts the existing elements to the right.

# ques 1 part 3
if 100 in L:
    L.remove(100)
print("After remove(100):", L)

removed_element = L.pop(2)
print("After pop(2):", L)
print("Element removed using pop():", removed_element)

# ques 1 part 4
L.sort()
print("Ascending order:", L)

L.sort(reverse=True)
print("Descending order:", L)

# ques 1 part 5
print("First three elements:", L[:3])
print("Last three elements:", L[-3:])

# ques 1 part 6
average = sum(L) / len(L)
greater_than_average = [x for x in L if x > average]
print("Average of L:", average)
print("Elements greater than average:", greater_than_average)
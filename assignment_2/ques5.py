roll_number = input("Enter your roll number: ")

digits = [int(digit) for digit in roll_number]
L = [digit * 10 for digit in digits]

print("\nQ5. DICTIONARY OPERATIONS")

name = input("Enter your name: ")
branch = input("Enter your branch: ")
age = int(input("Enter your age: "))
city = input("Enter your home city: ")
cgpa = float(input("Enter your CGPA: "))

my_dict = {
    "name": name,
    "roll_no": roll_number,
    "branch": branch,
    "age": age,
    "city": city
}

print("\nOriginal dictionary:")
print(my_dict)

# ques 5 part 1
my_dict["location"] = my_dict.pop("city")

print("\nAfter renaming city to location:")
print(my_dict)

# ques 5 part 2
my_dict["cgpa"] = cgpa

print("\nAfter adding CGPA:")
print(my_dict)

# ques 5 part 3
my_dict["age"] = my_dict["age"] + 1

print("\nAfter increasing age by 1:")
print(my_dict)

# ques 5 part 4
dict_pop = my_dict.copy()

removed_branch = dict_pop.pop("branch")

print("\nDictionary after deleting branch using pop():")
print(dict_pop)
print("Value returned by pop():", removed_branch)

# Delete branch using del
dict_del = my_dict.copy()

del dict_del["branch"]

print("\nDictionary after deleting branch using del:")
print(dict_del)

# pop() returns the removed value, while del only deletes the key-value pair.

# ques 5 part 5
print("\nKey-value pairs:")

for key, value in my_dict.items():
    print(key, "→", value)

# ques 5 part 6
print("\nChecking for email:")

if "email" in my_dict:
    print("Email:", my_dict["email"])
else:
    print("Email key does not exist.")

# ques 5 part 7
friend_dict = {
    "name": "Rahul",
    "roll_no": "12345678",
    "branch": "CSE",
    "age": 20,
    "city": "Delhi"
}

merged_dict = {**my_dict, **friend_dict}

print("\nFriend dictionary:")
print(friend_dict)

print("\nMerged dictionary:")
print(merged_dict)

# When the same key exists in both dictionaries,
# the value from the second dictionary wins.

# ques 5 part 8
string_values_dict = {
    key: value
    for key, value in my_dict.items()
    if isinstance(value, str)
}

print("\nDictionary containing only string values:")
print(string_values_dict)
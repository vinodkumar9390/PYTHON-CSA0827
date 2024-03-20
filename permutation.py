import itertools

def find_combinations(digits):
    combinations = itertools.permutations(digits)
    for combination in combinations:
        print(''.join(combination))

# Sample Input
digits = input("Enter 3 digits: ")

# Check if the input contains 3 digits
if len(digits) == 3 and digits.isdigit():
    find_combinations(digits)
else:
    print("Invalid input. Please enter exactly 3 digits.")

def is_mirror_number(num):
    # Convert the number to a string and reverse it
    reversed_num = str(num)[::-1]
    
    # Check if the reversed number is equal to the original number
    return str(num) == reversed_num

# Test cases
num1 = 121
num2 = 123
num3 = 1221

print("Number:", num1, "Is Mirror Number:", is_mirror_number(num1))  # Output: True
print("Number:", num2, "Is Mirror Number:", is_mirror_number(num2))  # Output: False
print("Number:", num3, "Is Mirror Number:", is_mirror_number(num3))  # Output: True

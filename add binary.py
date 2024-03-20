def add_binary(a, b):
   
    sum_decimal = int(a, 2) + int(b, 2)
    
    
    sum_binary = bin(sum_decimal)[2:]
    
    return sum_binary

# Test cases
a = "11"
b = "1"
print("Output:", add_binary(a, b))  # Output: "100"

a = "1010"
b = "1011"
print("Output:", add_binary(a, b))  # Output: "10101"

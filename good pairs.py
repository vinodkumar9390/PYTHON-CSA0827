def num_good_pairs(nums):
    # Create a hashmap to count occurrences of each number
    num_counts = {}
    for num in nums:
        if num in num_counts:
            num_counts[num] += 1
        else:
            num_counts[num] = 1
    
    # Calculate the number of good pairs
    good_pairs = 0
    for count in num_counts.values():
        if count > 1:
            good_pairs += count * (count - 1) // 2
    
    return good_pairs

# Test case
nums = [1, 2, 3, 1, 1, 3]
print("Output:", num_good_pairs(nums))

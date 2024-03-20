def min_jumps(nums):
    if not nums or len(nums) == 1:
        return 0
    
    n = len(nums)
    if nums[0] == 0:
        return -1
    
    max_reach = nums[0]
    steps = nums[0]
    jumps = 1
    
    for i in range(1, n):
        if i == n - 1:
            return jumps
        
        max_reach = max(max_reach, i + nums[i])
        steps -= 1
        
        if steps == 0:
            jumps += 1
            
            if i >= max_reach:
                return -1
            
            steps = max_reach - i
    
    return jumps

# Test case
nums = [2, 3, 1, 1, 4]
print("Minimum number of jumps:", min_jumps(nums))  # Output: 2

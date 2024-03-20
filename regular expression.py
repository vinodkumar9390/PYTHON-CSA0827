def is_match(s, p):
    # Create a 2D dp array to store the matching status
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    
    # Base case: empty string and pattern match
    dp[0][0] = True
    
    # Handle patterns with '*'
    for j in range(2, len(p) + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]
    
    # Fill the dp array
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (p[j - 2] == '.' or p[j - 2] == s[i - 1]))
    
    return dp[len(s)][len(p)]

# Test cases
s1, p1 = "aa", "a"
s2, p2 = "aa", "a*"
s3, p3 = "ab", ".*"
s4, p4 = "aab", "c*a*b"

print("s1:", is_match(s1, p1))  # Output: False
print("s2:", is_match(s2, p2))  # Output: True
print("s3:", is_match(s3, p3))  # Output: True
print("s4:", is_match(s4, p4))  # Output: True

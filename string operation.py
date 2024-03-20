def min_distance(word1, word2):
    # Initialize a 2D matrix to store the minimum number of operations
    dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
    
    # Initialize the first row and first column
    for i in range(len(word1) + 1):
        dp[i][0] = i
    for j in range(len(word2) + 1):
        dp[0][j] = j
    
    # Fill the matrix
    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
    
    return dp[len(word1)][len(word2)]

# Test cases
word1 = "horse"
word2 = "ros"
print("Minimum operations:", min_distance(word1, word2))  # Output: 3

word1 = "intention"
word2 = "execution"
print("Minimum operations:", min_distance(word1, word2))  # Output: 5
 
def max_profit(prices):
    n = len(prices)
    if n < 2:
        return 0

    
    dp1 = [0] * n
    dp2 = [0] * n

    # First transaction: Buy -> Sell
    min_price = prices[0]
    for i in range(1, n):
        min_price = min(min_price, prices[i])
        dp1[i] = max(dp1[i - 1], prices[i] - min_price)

    # Second transaction: Buy -> Sell
    max_price = prices[n - 1]
    for i in range(n - 2, -1, -1):
        max_price = max(max_price, prices[i])
        dp2[i] = max(dp2[i + 1], max_price - prices[i])

    # Calculate the maximum profit by combining the profits from both transactions
    max_profit = 0
    for i in range(n):
        max_profit = max(max_profit, dp1[i] + dp2[i])

    return max_profit

# Example usage:
prices = [3, 3, 5, 0, 0, 3, 1, 4]
print("Maximum profit:", max_profit(prices))


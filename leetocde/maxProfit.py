def maxProfit(prices):
    minPrice = math.inf
    max_profit = 0
    for i in range(len(prices)):
        if prices[i] < minPrice:
            minPrice = prices[i]
        else:
            max_profit = max(max_profit,prices[i] - minPrice)

    return max_profit

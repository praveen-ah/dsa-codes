def maxProfit(prices):
    profit = 0
    max_profit = 0
    buy = prices[0]
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit = prices[i] - prices[i-1]
            max_profit += profit
    print(max_profit)

prices = [7,1,5,3,6,4]
prices2 = [1,2,3,4,5]
print(maxProfit(prices))
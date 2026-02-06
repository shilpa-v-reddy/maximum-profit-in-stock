def find_profit(prices):
    if len(prices) <2:
        return 0
    
    min_price = prices[0]
    max_profit = 0

    for i in range(1,len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
            continue

        current_profit = prices[i] - min_price
        if current_profit > max_profit:
            max_profit = current_profit
    return max_profit
prices = [6,12,10,4,13]
print("maximum profit:", find_profit(prices))
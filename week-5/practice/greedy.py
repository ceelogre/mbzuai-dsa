def greedy(coins, amount):
  coins = sorted(coins, reverse=True)
  count = 0
  coins_used = []
  for coin in coins:
    while amount >= coin:
      amount = amount - coin
      coins_used.append(coin)
      count += 1
  
  return (count, coins_used)

print(greedy([1,2,5], 19))
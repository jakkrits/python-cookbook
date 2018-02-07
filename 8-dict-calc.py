prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
# flip value, key -> zip()

min_price = min(zip(prices.values(), prices.keys()))
print(min_price)

max_price = max(zip(prices.values(), prices.keys()))
print(max_price)

sorted_price = sorted(zip(prices.values(), prices.keys()))
print(sorted_price)
# be aware that zip() creates an iterator that can only be
# consumed once.

print('*' * 30)
print('as opposed to')

min_stock = min(prices, key=lambda k: prices[k])
min_price = prices[min(prices, key=lambda k: prices[k])]
print(min_stock)
print(min_price)
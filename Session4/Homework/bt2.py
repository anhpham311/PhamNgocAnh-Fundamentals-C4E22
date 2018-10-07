prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3, 
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15,
}

# For each key, print out the key along with its price and stock information.
for k in prices.keys():
    print(k)
    print("prices:",prices[k])
    print("stock:", stock[k])

#how much money you would make if you sold all of your food
total = 0

for k in prices.keys():
    revenue = prices[k] * stock[k]
    print(revenue)
    total = total + revenue

print(total)
    
    
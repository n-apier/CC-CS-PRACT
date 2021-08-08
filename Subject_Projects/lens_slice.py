# Your code below:
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]

pizza_and_prices.sort()
cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]
pizza_and_prices.pop()
pizza_and_prices.insert(4,[2.5, "peppers"])
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)

print(pizza_and_prices)
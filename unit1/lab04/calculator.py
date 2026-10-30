# Self-Assesment Questions:
# 1. The error that would occur is not that python would crash,
# but it would instead silently produce the wrong answer.

# 2. The modulo operator (%) in a real-world scenario in business is salary 
# expenses and having to divide them amoung employees, etc. It can help with
# finding the remaining amount of expenses available.

# 3. I feel like I am less confident in f strings, but I believe with
# enough practice I will be fine in time.

# Exercise 1:
price = 50 
quantity = 12
revenue = price * quantity

print(f"revenue: ${revenue:,.2f}") # thousands place

# Exercise 2:
cost = 32
price = 50
margin = (price - cost)/price # we want a float; the underlying variable NEVER changes

print(f"margin: {margin:.1%}") # percentage format

# Exercise 3:
margin_a = .36
margin_b = .25
product_a_wins = margin_a > margin_b

print(f"product A wins: {product_a_wins}")

# Exercise 4:
price = 150
margin = .35
is_premium = price > 100
good_margin = margin > .3

print(f"is_premium: {is_premium}")

use_product = is_premium and good_margin

print(f"use_product: {use_product}")

# Exercise 5:
print(17/5) # Computes the exact value, in decimal form (3.4).
print(17//5) # Rounds the value to a whole number (3).
print(17%5) # Calculates the remainder (2).

# Exercise 6:
product = input("enter product name:")
price = float(input("enter product price:"))
cost = float(input("enter product cost:"))
quantity = int(input("enter quantity sold:"))
discount = float(input("enter discount percentage:"))

revenue = price * quantity
discounted_revenue = revenue * (1 - discount)
gross_margin = (price - cost) / price
net_profit = discounted_revenue - (cost * quantity)

print(f"product: {product}")
print(f"revenue: ${revenue:,.2f}")
print(f"net revenue: ${discounted_revenue:,.2f}")
print(f"margin: {gross_margin:,.1f}")
print(f"net profit: {net_profit:,.2f}")

# Exercise 7:
BOX_SIZE = 24
items_ordered = int(input("number of items ordered:"))
full_boxes = items_ordered // BOX_SIZE
loose_items = items_ordered % BOX_SIZE
exact_fit = loose_items == 0

print(f"full boxes: {full_boxes}")
print(f"loose items: {loose_items}")
print(f"exact fit: {exact_fit}")
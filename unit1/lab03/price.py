# Exercise 5 
# type("12"), type(12), type (12.0), type(True)
# (‹class 'str'>, ‹class 'int'>, ‹class 'float'>, <class 'bool'›)
# Observation: When I typed ("5"+"3") it resulted in "53",
# but when I typed (5+3) I got 8 as my answer.

#Self-Assessment Questions
# 1. In Exercise #3, a TypeError occurs because you can’t do math in Python with a string and a number.
# So the price can’t be converted to a float from a string.

# 2. Python combines the strings and so it results in a new string “53”,
# input must always be converted before doing math because if not you’ll be given a new string.

# 3. In my future career using variables, types,
# and f-strings will create efficient summary documents and will make work more efficient.
# For example, if I need a balance statement, I could create one using the three components.
# Variables for revenue, expenses, dividends, and f-strings would help execute the formulas and mathematics.
# Types can help with identifying each variables within in the balance sheet. 


#  Exercise 1
product = "notebook" #str
unit_price = 4.99 #float
quantity = 12 #integer
in_stock = True #bool

print(type(product))
print(type(unit_price))
print(type(quantity))
print(type(in_stock))

total = unit_price * quantity
print(f"total: ${total:.2f}")

# Exercise 2 
print(f"{quantity} units of {product} at ${unit_price} each = ${unit_price * quantity: .2f}")

# Exercise 3 
product_in = input("product:")
price_in = float(input("unit_price:"))
quantity_in = int(input("quantity:"))

print(f"{quantity_in} units of {product_in} at ${unit_price:.2f} each = ${price_in * quantity_in:.2f}")

# Exercise 4 
unit_cost = 3.29
revenue = unit_price * quantity
margin = (unit_price - unit_cost) / unit_price 

print(f"product: {product}")
print(f"price: ${unit_price:.2f}")
print(f"quantity: {quantity}")
print(f"revenue: ${revenue:.2f}")
print(f"margin: {margin:.1%}")

# print(f"product: {product}\nRevenue: ${revenue:,.2f}\ncost: ${unit_cost:,.2f}\nmargin {margin:.1f}%")

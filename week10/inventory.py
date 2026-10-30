# Course: ISM2411 Section 4
# Author: Samhita Savaram
# Reflection Questions:
# 1. What surprised me the most about the exercises was that alphabetizing words is a little more complicated than it seems. Capitalized words come before lowercase words, even if they are not in alphabetical order when ignoring capitalization. Also, numbers and special characters are organized in a specific order.# 2. 
# 2. Python saves time because it does the tedious work for me. It does the calculations and finds what's in the middle. Alphabetizing lists is also so helpful and cuts time in Excel.

print("Exercise 1: Build a List") #!!!

inventory = ["pen", "notebook", "stapler", "tape", "marker"]

print(inventory)
print(len(inventory))

print("Exercise 2: Index Practice") #!!!

print(inventory[0])
print(inventory[-1])
middle = len(inventory) // 2
print(inventory[middle])

print("Exercise 3: Slicing Practice") #!!!

print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

print("Exercise 4: Modify") #!!!

inventory.append("envelope")
inventory.remove("tape")

inventory.sort()
print(inventory)

print("Exercise 5: Tuple Comparison") #!!!

coords = (40.7128, -74.0060)
try:
    coords[0] = 99
except TypeError as error:
    print("TypeError caught:", error)
    print("Tuples protect coordinates: a location should never change by accident.")

print(coords)

print("Exercise 6: Average List of Sales") #!!!

sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total /count

print(f"total: {total}")
print(f"count: {count}")
print(f"average: {average}")
print(f"best: {max(sales)}")
print(f"worst: {min(sales)}")

print("Exercise 7: Accumulator Pattern") #!!!

prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discount =[]
for price in prices:
    discount.append(round(price *.9, 2))

print("Original Prices:", prices)
print("Discount Prices:", discount)

print("Exercise 8: Filter Above Threshold")

sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []
for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print("High Sales:", high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales)/len(high_sales):.2f}")
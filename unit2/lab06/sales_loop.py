# 3 Self Assessment Questions
# 1. The accumulator pattern is using loops to build a result. To create an accumulator pattern, you need three steps. One, create a variable to store the result. Two, iterate and update the result in each loop. Three, print results. Each step is vital, as it tracks the result in each loop.
# 2. The length of the code in [for] is shorter than [while]. The trade-off of each approach is that the [for] loop is better for lists, whereas the [while] loop continues until it is met with stopping conditions.
# 3. My summer internship at the Community Food Pantry has to register a certain minimum number of families served, so we could use a loop to compute a summary for every month. The list contain the number of families that were served each month. Accumulating the total number of families and the average number of families per month. This will help determine if the minimum requirements were reached.

# Exercise 1
sales = [120, 80, 250, 175, 90, 410, 60, 215]
total = 0  #initialize
for sale in sales: 
    total += sale  #update
print(f"total: ${total}")

# Exercise 2
total = 0
count = 0
for sale in sales:
    total += sale
    count += 1

average =  total / count 
print(f"total: ${total}")
print(f"count: {count}")
print(f"average: ${average:.2f}")

# Exercise 3
current_max = 0 
for sale in sales:
    if sale > current_max:
        current_max = sale

print(f"largest sale: ${current_max}")

# Exercise 4
count_over_100 = 0
total_over_100 = 0 
for sale in sales:
    if sale > 100:
        count_over_100 += 1
        total_over_100 += sale

print(f"sales over $100: {count_over_100}")
print(f"total of those sale: ${total_over_100}")

# Exercise 5
for sale in sales:
    if sale > 400:
        print(f"alert: outlier found - ${sale}. stopping.")
    if sale <= 100:
        continue
    print(f"${sale}")

# Exercise 6
total = 0 
i = 0 
while i < len(sales):
    total += sales[i]
    i += 1
print(f"total (while loop): ${total}")

# Exercise 7 

sales = [120, 80, 250, 100, 200, 75]

for sale in sales:
    if sale >= 200:
        discount = 0.10
    elif sale >= 100:
        discount = 0.05
    else:
        discount = 0

    disounted_price = sale * (1 - discount)

    print(f"${sale:.2f} -> discount: {discount:.0%} -> final price: ${disounted_price:.2f}")


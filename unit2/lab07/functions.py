# Self-Assessment Questions 
# 1. The first bug I personally spotted was the missing colon. I found it on my own as it just looked incomplete. What it tells me about my current debugging skills is I can see small incorrect code/statements.
# 2. apply_discount(price, tier) means it is using two different inputs. In result it will produce the discount and total price. Yes a collage could tell.
# 3. AI DISCLOSURE: I used AI to help debug minor issues within exercise five's code. The AI helped me notice issues that I would've been unable to spot on my own.

# Exercise 1: 
# define calculate tax function
def calculate_tax(price, rate):
    return price * rate

# calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"tax on $100 at 7% ${tax1:.2f}") # $7.00
print(f"tax on $100 at 8% ${tax2:.2f}") # $20.00

# another way, without creating new variables
print(f"another tax: ${calculate_tax(100, 0.07):.2f}")
print(f"another tax: ${calculate_tax(250, 0.08):.2f}")

# Exercise 2:
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

 # calling the function

price = 200
tiers = ["gold", "silver", "bronze", "none"]

for tier in tiers:
    print(f"{tier}: ${apply_discount(price, tier):.2f}")

# Exercise 3:
# write it out manually first, the refactor into a function

discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax

print(f"after gold discount: ${discounted:.2f}")
print(f"after tax: ${after_tax:.2f}")

# refactor into a function

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

print(f"final price: ${final_price(200, "gold", 0.07):.2f}")

# Exercise 4:
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"price: ${price:.2f}, tier: {tier}, final: ${total:.2f}")

# Exercise 6:
x = 100

def double_it():
    global x
    x = 999
    return x * 2

print(x)
print(double_it())
print(x)

# Exercise 5: 
# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

# ERROR ABOVE!!
# 1. Total variable is replaced by sales. 
# 2. AI explanation: Current sale is assigned to total in the loop, and so it only produces the last item. This is not calculating the total.
# 3. The addition symbol shows that it will calculate a total of sales.
# 4. AI found the mistake and helped debug it!

count = 0
for sale in sales:
# ERROR FOUND ABOVE!!
# 1. No colon (:) at the end of the for statement.
# 2. AI explanation: The for statement is incomplete, and so it results in a SyntaxError. 
# 3. Added a colon to complete the for statement.
# 4. The AI's found mistake does match the bug within the code. 

    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):
# ERROR ABOVE!!
# 1. There should not be a equal sign.
# 2. IndexError, because when i reaches 5 it does not exist within the 0 to 4 range.
# 3. Change <= to < (continous loop)
# 4. AI found the issue, but confused what the fix should specifically be. 

    print(sales[i])
    i += 1

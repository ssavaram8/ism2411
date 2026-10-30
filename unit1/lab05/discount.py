# Self-Assessment Questions:
# 1. Python is checking if order_total = 350 meets the conditions, running top to bottom. 350 meets the conditions of elif total >= 200 and a 10% discounted total price is presented ($315).

# 2. Elif and if, are two independent statements so python can check them individually. In the scenario presented the conditions are both true. Not every elif/if condition statements will be true, it can vary.

# 3. I encounter systems that use tier condition logic when I am ordering food through GrubHub. I can either use bullbucks or exchange for a mealswipe. Python has changed how I view that system because 
# I now realize how when I go to checkout, it is checking if I have enough funds or meal swipes through conditions.

# Exercise 1:
total = float(input("Enter cart total: $"))

if total >= 500:
    discount = 0.15
elif total >= 200:
    discount = 0.10
elif total >= 100:
    discount = 0.05
else:
    discount = 0

final = total * (1 - discount)
print(f"Discount: {discount*100:.0f}%")

# Exercise 3:
region = "South"
extra_discount = 0

if region == "South" and total >= 100:
    extra_discount = 0.02

    print("Region bonus applied: additional 2% off")

# Exercise 1: Redirect
final_discount = discount + extra_discount
final = total * (1 - final_discount)

print(f"Discount: {final_discount:.1%}")
print(f"Final price: ${final:,.2f}")

# Exercise 2: Redirect
if final > 1000:
    status = "manager_approval_required"
else:
    status = "auto_approved"

print(f"Status: {status}")

# Exercise 4:
customer_type = "wholesale"
# if region == "South":
#   if total >= 100:
#       if customer_type == "wholesale":
#           extra_discount + 0.03

if region == "South" and total > 100 and customer_type == "wholesale":
    extra_discount = 0.03

print(extra_discount)

# Exercise 5:
amount = 120000
if amount <= 0:
    print("SUSPICIOUS")
elif amount < 100000:
    print("NORMAL")
else: 
    print("LARGE - REVIEW REQUIRED")

# Exercise 6:
total_spent_this_year = 2500
orders_this_year = 6
has_outstanding_balance = False

qualifies_by_spending = total_spent_this_year > 2000
qualifies_by_orders = orders_this_year > 10

vip_upgrade = (qualifies_by_spending or qualifies_by_orders) and not has_outstanding_balance

print(f"VIP upgrade: {vip_upgrade}")
"""
Write a Python program named discount.py that gets a customer's subtotal as input 
and gets the current day of the week from your computer's operating system. Your 
program must not ask the user to enter the day of the week. Instead, it must get 
the day of the week from your computer's operating system.
If the subtotal is $50 or greater and today is Tuesday or Wednesday, your
program must subtract 10% from the subtotal. Your program must then compute the 
total amount due by adding sales tax of 6% to the subtotal. Your program must 
print the discount amount if applicable, the sales tax amount, and the total amount due.
"""
from datetime import datetime

current_date = int(datetime.now().weekday())
# current_date = 4
subtotal = float(input("What is your subtotal? "))

def sales_tax():
    tax = subtotal * .06
    print(f"Sales tax amount: {tax}")
    return tax

def discount():
    if subtotal >= 50 and (current_date == 1 or current_date == 2):
        deal = round(subtotal * .1, 2)
        new_total = subtotal - deal  
        print(f"discount: {deal}")
        return new_total
    else: 
        return subtotal
        
def difference():
    if subtotal < 50 and (current_date == 1 or current_date == 2):
        distance = round(50 - subtotal, 2)
        print(distance)
    else:
        print("You get the discount")

total = sales_tax() + discount()

print(f"Total: {total:.2f}")
    

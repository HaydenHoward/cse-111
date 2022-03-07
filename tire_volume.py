"""
Write a Python program named tire_volume.py that reads from the keyboard the three 
numbers for a tire and computes and outputs the volume of space inside that tire.
"""
import math
from datetime import datetime

width = float(input("Enter the width of the tire in mm (ex 205): "))
ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))
  
volume = round(math.pi * width**2 * ratio * (width * ratio + 2540 * diameter) / 10000000000, 2)
print(f"The approximate volume is {volume} liters")
current_date = datetime.now()
print(f"{current_date:%Y-%m-%d}")

with open("volumes.txt", "at") as dimens_file:
    print(f"{current_date:%Y-%m-%d},", end=" ", file=dimens_file)
    print(f"{width:.0f}, {ratio:.0f}, {diameter:.0f}, {volume},", end=" ", file=dimens_file)

    buy = input("would you like to buy tires this size? (y/n)").lower()
    if buy == "y":
        name = input("What is your name? ").title()
        number = input("What is your phone number? ")
        print(f"{name}, {number}", file=dimens_file)
        print("Thank you we will contact you shortly.")


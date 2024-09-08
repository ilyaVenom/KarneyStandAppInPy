# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 07:55:19 2024
@author: segal
"""
# making Koncession stand game:
# practicing dictionaries: 

# movie stand list of items    
menu = {"hotdog": 1.00,
        "popcorn": 1.50,
        "soda": 1.75,
        "water": 2.00,
        "pizza": 5.00}

# where the item goes first
cart = []
total = 0
# next decrotive txt:
print("++++++++++ MENU ++++++++++++")
for key, value in menu.items():
    print(f"{key:10} : ${value:.2f}")
print("++++++++++++++++++++++++++++")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        
#print(cart)
print()
print("++++++++++ YOUR ORDER +++++++++++++++")
for food in cart:
    total += menu.get(food)
    print(food, end=" + " )

print()
print(f"Total is: ${total:.2f}")        
    
    



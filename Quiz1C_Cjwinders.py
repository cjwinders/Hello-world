# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 14:43:23 2024

@author: casey
Quiz type: version c
"""
#Prompting user to enter item information
name = input("Enter the name of the item: ")
quantity = int(input("Enter the number of the item in stock: "))
price = float(input("Enter the price for one unit: $"))
#Calculating total inventory
total_inventory = quantity*price
#Rounding the inventory to 2 decimal places
round(total_inventory, 2)
#Printing the total inventory with a dollar sign
print("The total value of the inventory for Laptop is: $" +str(total_inventory))



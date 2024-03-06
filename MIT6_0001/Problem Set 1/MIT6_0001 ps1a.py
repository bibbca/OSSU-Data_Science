#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 20:39:36 2024

@author: Caleb Bibb

MIT6_0001 Problem Set 1a

Your program should ask the user to enter the following variables:
1. The starting annual salary (annual_salary)
2. The portion of salary to be saved (portion_saved)
3. The cost of your dream home (total_cost)
"""

annual_salary = float(input("Enter your annual salary ($):"))
portion_saved = float(input("What portion are you saving? (Decimal)"))
total_cost = float(input("Enter total cost of dream home ($):"))

# Assumptions:
portion_down_payment = 0.25
current_savings = 0
monthly_salary = annual_salary / 12
r = 0.04    # annual rate of return
number_of_months = 0

while current_savings < total_cost * portion_down_payment:
    current_savings += current_savings*r/12 # appreciation of investments
    current_savings += portion_saved * monthly_salary
    number_of_months += 1

print("Number of Months:", number_of_months)

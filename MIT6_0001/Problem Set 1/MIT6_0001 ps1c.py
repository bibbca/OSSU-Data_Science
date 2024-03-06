#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 21:19:51 2024

@author: Caleb Bibb

MIT6_0001 Problem Set 1c

Use Bisection search to find a good savings rate.
"""

annual_salary = float(input("Enter your annual salary ($): "))

# Assumptions:
total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment = 0.25 # percentage of down payment
current_savings = 0 # starting savings
monthly_salary = annual_salary / 12
r = 0.04    # annual rate of return
epsilon = 100
number_of_steps = 0
lower_bound = 0 # percentage points 0.000%
upper_bound = 10000 # percentage points 100.00%

amount_to_save = total_cost * portion_down_payment
portion_saved = (upper_bound + lower_bound) // 2 # initial guess
while abs(current_savings - amount_to_save) >= epsilon:
    current_savings = 0
    monthly_salary = annual_salary / 12
    number_of_months = 0
    while number_of_months < 36:
        current_savings += current_savings*r/12 # appreciation of investments
        current_savings += (portion_saved / 10000) * monthly_salary
        number_of_months += 1
        if number_of_months % 6 == 0:
            monthly_salary += monthly_salary * semi_annual_raise
    if amount_to_save > current_savings: # Not enough money saved
        lower_bound = portion_saved # raise the lower bound
    else: # excess money saved
        upper_bound = portion_saved # lower the upper bound
    portion_saved = (upper_bound + lower_bound) // 2 # new guess
    number_of_steps += 1
    if number_of_steps > 100:
        break
if portion_saved == upper_bound or number_of_steps == 101:
    print("Not possible with current salary. :(")
else:
    print("Best Savings Rate = ", portion_saved)
    print("Steps in Bisection Search:", number_of_steps)

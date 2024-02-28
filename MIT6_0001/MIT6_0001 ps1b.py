#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 21:19:51 2024

@author: Caleb Bibb

MIT6_0001 Problem Set 1b
"""

annual_salary = float(input("Enter your annual salary ($): "))
portion_saved = float(input("What portion are you saving? (Decimal): "))
total_cost = float(input("Enter total cost of dream home ($): "))
semi_annual_raise = float(input("What's your raise? (Decimal): "))
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
    if number_of_months % 6 == 0:
        monthly_salary += monthly_salary * semi_annual_raise

print("Number of Months:", number_of_months)
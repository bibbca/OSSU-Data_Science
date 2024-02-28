#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 20:27:16 2024

@author: Caleb Bibb

MIT6_0001 Problem Set 0

Write a program that does the following in order:
1. Asks the user to enter a number “x”
2. Asks the user to enter a number “y”
3. Prints out number “x”, raised to the power “y”.
4. Prints out the log (base 2) of “x”.
"""

import numpy

x = float(input("Enter a number x:"))
y = float(input("Enter a number y:"))

power = numpy.power(x,y)
print("x**y = ", power)

log = numpy.log2(x)
print("log(x) = ", log)
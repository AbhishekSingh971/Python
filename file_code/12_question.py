# Write a program that defines a function large in a module which will be used to find larger of two values and called from code in another module
from 12large import *

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
c = 12large.large(a, b)
print(c)
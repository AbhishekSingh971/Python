# Write a program to display Bar graphs or Pie chart using Matplotlib

# Import libraries
from matplotlib import pyplot as plt
import numpy as np
 
 
# Creating dataset
cars = ['AUDI', 'BMW', 'FORD',
        'TESLA', 'JAGUAR', 'MERCEDES']
 
data = [23, 17, 35, 29, 12, 41]
 
# Creating plot
plt.figure(figsize =(7, 7))
plt.pie(data,cars,4)
 
# show plot
plt.show()
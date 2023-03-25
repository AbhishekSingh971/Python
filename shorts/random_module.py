# based on the random module 
import random


# write a program to print directories, functions in the random module
print(dir(random))

# write a program to randomly pick an element from a list;
list = [1,2,3,4,5,6,7,8,9]
print(random.choice(list))  # chice is used to randomly pick an element from an array or a list

# write aa program to shuffle the list of item
list = [1,2,3,4,5,6,7,8,9]
print(random.shuffle(list))

# diffrent between randrange and randint


# how can you genrate a floting random number in a range
print(random.uniform(1,100))

# how to genrate a random number between 0 and 1;
print(random.random())

#
x=3
n=random.randint(2,x)
for i in range(n):
    print( i,"#", i+1)

#
list = [14,62,30,57,91]
str=('simply')
print(random.choice(list)," and ",random.choice(str))

#
n1 = random.randrange(1,10,2)
n2 = random.randrange(1,10,3)
print(n1," and ",n2)

#
stringN="SimplyCoding"
char_list = list(stringN)
print(random.shuffle(char_list))

stringN = ' '.join(char_list)
print(stringN)
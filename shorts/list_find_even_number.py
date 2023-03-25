# write a function to print even number in loop
def even(list):
    for i in list:
        if(i%2 == 0):
            print(i, " is even")

list = [1,2,3,4,5,6,7,8,9,10]
even(list)
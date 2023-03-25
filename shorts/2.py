# write a function to print the sum of all the element in a list
def sum(list):
    sum = 0
    for i in list:
        sum+=i
    print(sum)

list = [1,2,3,4,5,6]
sum(list)

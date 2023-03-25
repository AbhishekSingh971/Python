# read the random dictionary and display the key in a sorted order
# dic = {'1':'abhi','2':'ansh','3':'rohan','4':'aman'}


# write a program to find product of all element of a list
h1 = 6
list = [1,2,3,4,5,h1]
sum = 1
for i in list:
    if(i%2!=0):
        sum *= i
print(sum)

# given two list l1 and l2 and you have to create 3list containing l1 and l2
# l1 = [1,2,3,4,5]
# l2 = [6,7,8,9,10]
# l3=[]
# for i in range(len(l1)):
#     l3[i]=l1[i]+l2[i]
# print(l3)

# crate a dictionary and convert that dictionary into a list
dic = {'1':'abhi','2':'ansh','3':'rohan','4':'aman'}
l4 = []
for i in dic:
    l4.extend([i,dic[i]])
print(l4)
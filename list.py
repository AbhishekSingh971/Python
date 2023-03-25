from filecmp import cmp


list1 = [1, 2, "3", 4]
print(list1)

# we can update single or multiple element of list by giving slice on left hand side of the assignment operator
list1[1]=4
print(list1)
list1[1:3] = [2, 3]
print(list1)

#append()
list2 = [1, 2, 7, 8, 6]
list2.append([600, 700])
print(list2)

#delete() : it is used to delete element from the list.
del(list2[2])
print(list2)

#concatination
print([1,2,3]+[4,5,6])

l1 = [1, 2, 3]
if 3 in l1:
    print("yes")

# built in list(): 
# ----------------------------- 1 -------------------------------------
# cmp()
#case 1: When a list contains just integers
#case 2: When comparision is made
#case 3: When no. by no. comparision is done from left to right, if we get larger no. at any particular index, 1 is returned and further comparision i stopped

# l = [2,3,5]   It show error
# r = [2,3,5]
# b = cmp(l,r)
# print(b)

# ----------------------------- 2 -------------------------------------
# len()

# ----------------------------- 3 -------------------------------------
# max()
l1 = [1,2,3]
l2 = [4,5,6]
print(max(l1 , l2))

# ----------------------------- 4 -------------------------------------
# count()

# ----------------------------- 5 -------------------------------------
#extend() : it append the containts of a list to another list.
l1 = [1,2,3]
l2 = [4,5,6]
l1.extend(l2)
print(l1)

# ----------------------------- 5 -------------------------------------
# index()
any
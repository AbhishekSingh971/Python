# write a program to merge two dictionary
dict = {"a": 1, "b":2}
dict2 = {"x":4, "y":5}
for i in dict2:
    dict[i] = dict2[i]

print(dict)
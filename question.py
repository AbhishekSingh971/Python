# write a program to convert a key value list in flat dictionary

dic = {'month' : [1, 2, 3], 'name' : ['Jan', 'Feb', 'March']}
# a = dict(zip(dic['month'], dic['name']))
# print(a)

# or

dic1 = {}
lis = list(dic.values())
x=lis[0]
y=lis[1]

for i in range(len(x)):
    dic1[x[i]]= y[i]

print(dic1)



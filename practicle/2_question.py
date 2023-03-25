list = [1,2,3,4,5]
item = int(input("enter the number to insert: "))
index = int(input("enter the index numbe to insert :"))
def insert(lst, item, n):
    lst.append(item)
    for i in range(len(lst) -1, n -1):
        lst[i], lst[i-1] = lst[i-1], lst[i]
    return lst

a = insert(list,item,index)
print(a)
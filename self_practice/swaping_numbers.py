def swap(lis, start, end):
    size = len(lis)
    
    temp = lis[start]
    lis[start] = lis[end]
    lis[end] = temp
    return lis

n = int(input("Enter the number of list item : "))
lis = []
# lis.extend(ls[i]= int(input()) for i in range(0,n))
# print(lis)
for i in range(0,n):
    lis.append(int(input()))

print(lis)
print("---------------Swap---------------")
start = int(input("enter the first number : "))
end = int(input("enter the end number : "))

sw = swap(lis, start-1, end-1)
print(lis)

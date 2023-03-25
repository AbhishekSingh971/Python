# write a program to check a number is plendrom or not

a = str(input())
b=list(a)
bool = False

for i in range(0,len(a)):
    if(a[i] == b[len(a)-(i+1)]):
        bool=True
    else:
        bool=False
        
if(bool == True):
    print("palindrom")

else:
    print("not palindrom")


# 2 option
a = str(input())
b=""
for i in a:
    b=i+b
if(a==b):
    print("yes, it is palindrom")
else:
    print("no, it is not palindrom")
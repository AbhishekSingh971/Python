a = 10
flag = True
for i in range(2,a):
    if(a%i==0):
        flag = False
        break
    else:
        flag == True
if(flag == False):
    print("not prime")
else:
    print("prime")
    
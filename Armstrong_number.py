a = 153
sum = 0
while(a>0):
    n = a%10
    sum += n**3
    print(sum)
    a//=10
print("this is the armstrong no.",sum)
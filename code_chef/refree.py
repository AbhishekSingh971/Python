t = int(input())
for i in range(t):
    a,b,c,d = map(int, input().split())
    sum = a+b+c+d
    if(sum >=1):
        print("out")
    else:
        print("in")
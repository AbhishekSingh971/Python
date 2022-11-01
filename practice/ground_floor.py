# Two friends Chef and Chefina are currently on floors AA and BB respectively. They hear an announcement that prizes are being distributed on the ground floor and so decide to reach the ground floor as soon as possible.

# Chef can climb down XX floors per minute while Chefina can climb down YY floors per minute. Determine who will reach the ground floor first. In case both reach the ground floor together, print Both.


t = int(input())
while(t):
    a,b,x,y = map(int, input().split())
    if(a*x == b*y):
        print("both")
    elif(a*x >= b*y):
        print("chef")
    else:
        print("chefina")
    t -= 1
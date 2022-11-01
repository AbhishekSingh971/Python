# Chef has scored A, B,A,B, and CC marks in 33 different subjects respectively.

# Chef will fail if the average score of any two subjects is less than 3535. Determine whether Chef will pass or fail.

t = int(input())
while(t):
    a,b,c = map(int, input().split())
    x=(a+b)/2
    y=(b+c)/2
    z=(a+c)/2
    if(x>=35 and y>=35 and z>=35):
        print("pass")
    else:
        print("fail")
    t-=1
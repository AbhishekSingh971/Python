# write a function to claculate the factorial of a number
def fact(a):
    mul = 1
    for i in range(1,a+1):
        mul *= i
    print(mul)
a = int(input())
fact(a)
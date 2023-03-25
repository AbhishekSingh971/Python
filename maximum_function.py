# write a program that define a function large in a module which will be use to find larger of two values and print it

def large(a,b):
    if(a>b):
        print(a)
    else:
        print(b)

a,b = map(int,input().split())
large(a,b)


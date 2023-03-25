# write a program to find a key of the minimum value in the key

dict = {"a": 1, "b":2, "c":3, "d":4, "e": 5}
value=0
for i in dict.values():
    if(value>=i):
        value=i
        
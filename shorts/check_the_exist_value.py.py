# write a program to check if a value exist in a dictionary or not
dict = {"a": 1, "b":2, "c":3, "d":4, "e": 5}
a = int(input())
# for i in dict.values():
#     if(a == i):
#         print("yes")
#         break 
#     else:
#         print("no")


# ---------------------------or------------------------------
print(a in dict.values())
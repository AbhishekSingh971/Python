lower = int(input("Enter the lower value : "))
upper = int(input("Enter the upper value : "))
flag = False
print("The Prime numbers between ", lower, " to ", upper, " are : ")
for num in range(lower, upper+1):
    if num > 1:
        for i in range(2, num):
            if(num % i == 0):
                flag = False
                break
            else:
                flag = True
        if flag == True:
            print(num, " is Prime number")
        else:
            print(num, " is not a prime number")

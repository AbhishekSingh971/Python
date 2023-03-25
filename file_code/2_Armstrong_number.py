x = int(input("Enter the number : "))
a = x
sum = 0
while(a > 0):
    n = a % 10
    sum += n**3
    print(sum)
    a //= 10
if(sum == x):
    print(x, " is an Armstrong number")
else:
    print(x, " is not an Armstrong number")

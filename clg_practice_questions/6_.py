list = [1,2,3,4,5,6,7,8,9,10,11]
prime = 0
notPrime = 0
# even = 0
# odd = 0

# for i in list:
#     if(i%2==0):
#         even += i
#     else:
#         odd += i

# print("sum of even number : ",even)
# print("sum of odd number : ",odd)


# for i in list:
#     if(i==2 or i==3 or i==5 or i==7 or i==11):
#         prime += i
#     elif(i%2==0 or i%3==0 or i%5==0 or i%7==0 or i%11==0):
#         notPrime += i
#     else:
#         prime += i

# print(prime)

sum = 0
for j in list:
    i=2
    while(i< j//2):
        if(j%i == 0):
            print("not a prime")
        else:
            print("prime")
            sum += j
            break

print(sum)


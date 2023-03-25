# write a program to take input as roll no. ,name and marks and perform thet following opreation using functions:
 # 1.update the marks 
 # 2.delete the record
 # 3.display the record
 # 4.append the record
 # 5.search the record
def addi(a,b,c,dic):
    # dic[a] : list(b,c)
    dic.update({a : [b, c]})

b = ""
dic = {}
while(b!="false"):
    b = str(input("Enter the name of student : "))
    a = int(input("Enter the roll no. : "))
    c = int(input("Enter the marks of student : "))
    if b!="false":
        addi(a,b,c,dic)

print(dic)

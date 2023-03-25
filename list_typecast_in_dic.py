def convert(a):
    dic = {a[i]:a[i+1] for i in range(0,len(a),2)}
    return dic

a =[1,'a',2,'b',3,'c']
print(convert(a))


a =[1,'a',2,'b',3,'c']
dic1={}
for i in range(0,len(a),2):
    dic1.update({a[i]:a[i+1]})

print(dic1)


b=[1,2,3,4,5]
c=['a','b','c','d','e']
dic2={}
for i in b:
    for j in c:
        dic2[i] = j
        c.remove(j)
        break
print(dic2)

dic3={2:'apple',1:'mango',3:'orange',4:'banana'}
for i in sorted(dic3.keys()):
    print(i,":",dic3[i])
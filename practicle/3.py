list1 = [[1,2,[3,4]],5]
list2 = []

def flat(list1):  
  for i in list1: 
    if type(i) == list: 
      flat(i) 
    else: 
      list2.append(i) 

flat(list1) 
print(list2)





dict = {2:"a",1:"b",3:"c",4:"d"}
#write a progeram to print the key and values of a dictonary
#print(dict.keys())
#print(dict.values())
# write a program to print key in the dictonary in sorted order
#print(sorted(dict.keys()))
# write a program to print key and value in sorted order by key
for i in sorted(dict.keys()):
    print(i, dict[i], sep=",")
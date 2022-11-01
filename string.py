str = "hello, hello world"
print(str.count("hello",0,10))

str1 = "this is an example"
print(str1.find("exam"))
print(str.endswith("hello",0,12))
print(str1.isalnum())
print(str1.isdigit())
print(str1.isalpha()) # It is check for the string is alphabet or not
print(str1.istitle()) # It is check for the first letter is capital or not
print(str1.isupper()) # It is check for the first letter is upper or not
print(len(str1))
print(str1.replace("this","It")) # It replaces all accrences of old string with 0 & 1
print(str1.isspace()) # It returns true if the string is containg white spaces
print(str1.swapcase()) # it inverse the case for all character in a string
print(str1.split(" ")) # it split the string according to the delimiter and return the list of strings

s = "_"
seq =("a","b","c")
print(s.join(seq)) # It returns a string in which string elemenet of sequence have been join by str sequence

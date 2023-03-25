words = 0
string = input('Please enter a string: ')
for word in string.split(' '):
    words += 1
print('The number of words in the string is :', words)
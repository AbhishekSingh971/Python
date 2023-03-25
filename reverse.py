string = str(input("Enter the word : "))

res = " ".join(reversed(string.split(" ")))

print(res)
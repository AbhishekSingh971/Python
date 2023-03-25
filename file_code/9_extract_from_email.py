str12 =str(input("Enter the email ID : "))
 
# printing original string
print("The original string is : " + str(str12))
 
# slicing user name using slicing
userName = str12[: str12.index('@')]

# slicing domain name using slicing
domainName = str12[str12.index('@') + 1 : ]
 
print("The extracted user name : " + str(userName))
print("The extracted domain name : " + str(domainName))

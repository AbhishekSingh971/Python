#create a dictionary whose keys are month nammes and whose values are the numbers of day in the corresponding months.
dic={"January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30, "July": 31, "August": 31, "September": 30, "October": 31, "November": 30, "December": 31}

# 1.Ask the user to enter a month name and use the dictionary to tell them how many days are in the month
a=str(input("Enter the month name : "))
print(a," : ",dic[a])

# 2.Print out all keys in the alphabetically order
print(sorted(dic))

# 3.Print out all the months with 31 days
print( "3.----Month which have 31 days are---- ")
for i in dic :
    if dic [ i ] == 31 :
        print( i )

# 4.Print out the key value pairs sorted by number of days in each month
print("4.----Month according to number of days ---")
print("feb")
for i in dic :
    if dic[ i ] == 30 :
        print(i)
for i in dic :
    if dic [ i ] == 31 :
        print( i)

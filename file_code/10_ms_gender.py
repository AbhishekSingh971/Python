def pre(name,gender):
    if (gender == 'M' or gender == 'm'):
        print("Mr.",name)
    elif (gender == 'F' or gender == 'f'):
        print("Ms.",name)
    else:
        print("Please enter only M or F in gender")

#Asking the user to enter the name
name = input("Enter your name: ")

#Asking the user to enter the gender as M/F
gender = input("Enter your gender: ")

pre(name,gender)

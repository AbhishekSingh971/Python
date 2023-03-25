fo = open("./file_code/13.txt", "rb+")

# Print the initial position
print ("Current Position: ", fo.tell())

# move the cursor to 4th position
fo.seek(4)
print ("Current Position: ", fo.tell())

#Display next 5 characters
print(fo.read(5))

# Move the cursor to the next 10 characters
fo.seek(10,1)

# Print the current cursor position
print ("Current Position: ", fo.tell())

# Print next 10 characters from the current cursor position
print(fo.read(10))


# Close opend file
fo.close()
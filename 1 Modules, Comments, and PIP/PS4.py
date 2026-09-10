print ("Que. 4 - Write a python program to print the contents of a directory using the os module. Search online for the function which does that.")


import os

# isse hum C drive ke kisi folder ke andar ke files aur folders ko dekh sakte hain
path = "."

# Get list of files and directories
contents = os.listdir('/intel')

# Print each item
for item in contents:
    print(item)
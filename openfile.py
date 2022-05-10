myfile = open("myfile.txt", "a") # a means open in append mode
file = ""
for line in myfile:
    print(line.rstrip()) # rstrip removes carriage returns and space
    file += line


choice = input("Would you like to add to the file y/n :")
if choice == "y":
    usertext = input("Enter text : ")
    file += usertext
    print("The new text file is :")
    print(file)
    #for i in file:
        #print(i, file = myfile)

print(file)

myfile.close()
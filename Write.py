#Write a single string
f=open("one.txt","w")
f.write("Hello \n")
f.write("Welcome to Python file handling\n")
f.write("Learning is fun!!\n")
f.close()

#ex :2
f=open("one.txt","w")
f.write("New content only.\n")
f.close()

#Append
f=open("one.txt","a")
f.write("This line is added at the end.\n")
f.close()
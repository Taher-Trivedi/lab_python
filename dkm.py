src=open("hello.txt","r")
data = src.read()
src.close()

dst = open("welcome.txt","w")
dst.write(data)
dst.close()
print("file copied successfull")

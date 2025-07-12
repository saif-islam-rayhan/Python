file = open("data.txt", "w")  
file.write("Hello, Rayhan!\n")
file.write("You are learning Python.\n")


file.close()
file=open("data.txt","r")
content=file.read()
print(content)
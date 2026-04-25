file =open("geek.txt" , "r")
print(file.read());
file.close()



#  creating  a  text File  

createFile = open("tanya.txt" , "w");
print (open("tanya.txt" , "r").read() == "") 

#  reading and writing the file
myfile = open("tanya.txt" , "w")
myfile.write("tanya you are the best for DSA")
myfile.close()


#  lets  read the content of  the file now 
myfile = open("tanya.txt" , "r")
print(myfile.read())






# appending content too the file 

myfile = open("tanya.txt" , "a")
myfile.write("..>> visit gfg for more feature ")
myfile.close()

#  reading thefile
myfile = open("tanya.txt" , "r") 
print(myfile.read())




#  checking file properties 
myfile = open("tanya.txt" , "r")
print(myfile.name)
print("Mode ",myfile.mode)
print("Is file closed ? ",myfile.closed )
myfile.close()
print("Is file closed ? ",myfile.closed )







# Using with statement to open a file
with open("tanya.txt", "r")as myfile:
    print(myfile.read())


     #  handling exception when closing a file 
try:
    myfile = open("tanya.txt" , "r")
    print(myfile.read())
finally:    myfile.close()

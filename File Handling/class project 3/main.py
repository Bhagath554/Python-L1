file = open("c:/Users/Admin/Desktop/Python L1/File Handling/Hi.txt",'r')
Counter = 0

content = file.read()

CoList = content.split("\n")

for i in  CoList:
        if i :
                   counter =+1
print("Hello")
print(Counter)
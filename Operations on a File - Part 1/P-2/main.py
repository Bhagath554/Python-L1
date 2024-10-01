file = open('c:/Users/Admin/Desktop/Python L1/Operations on a File - Part 1/Hi.txt','r')
print("Reading First line")
print(file.readline())
file.close()

file = open('c:/Users/Admin/Desktop/Python L1/Operations on a File - Part 1/Hi.txt','r')
print("Reading multiple lines")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

file = open('c:/Users/Admin/Desktop/Python L1/Operations on a File - Part 1/Hi.txt','r')
print("Looping through the Lines...")
for line in file:
 print(line)
file.close()
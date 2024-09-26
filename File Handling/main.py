file = open("c:/Users/Admin/Desktop/Python L1/File Handling/Hi.txt",'r')
print("File in Read Mode")
print(file.read())
file.close()

file_wr = open("c:/Users/Admin/Desktop/Python L1/File Handling/Hi.txt",'w')
print("File in write Mode")
file.write("Hello I am Penguine")
file_wr.close()

file_ap = open("c:/Users/Admin/Desktop/Python L1/File Handling/Hi.txt",'a')
print("\nFile in append Mode")
file.write("Hello I am Penguine")
file_ap.close()
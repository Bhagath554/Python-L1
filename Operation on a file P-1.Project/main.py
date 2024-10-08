file1 = open('c:/Users/Admin/Desktop/Python L1/Operation on a file P-1.Project/Bye.txt','r')
file2 = open('c:/Users/Admin/Desktop/Python L1/Operation on a file P-1.Project/so.txt','w')

print("Reading Multiple lines of File1")
print(file1.readline())
print(file1.readline())
print(file1.readline())
print(file1.readline())






file1 = open('c:/Users/Admin/Desktop/Python L1/Operation on a file P-1.Project/Bye.txt','r')
file2 = open('c:/Users/Admin/Desktop/Python L1/Operation on a file P-1.Project/so.txt','w')
print("Now Removing lines in the file")

for line in file1.readlines():

         if not (line.startswith('Basketball')):
            print(line)

            file2.write(line)



file1 = open('c:/Users/Admin/Desktop/Python L1/Operation on a file P-1.Project/Bye.txt','r')
file2 = open('c:/Users/Admin/Desktop/Python L1/Operation on a file P-1.Project/so.txt','w')
cont = file1.readlines()
type(cont) 
print(type(cont))
print("Removing Even Lines from the file")

for i in range(1,len(cont)):
      if (i % 2 == 0):
              file2.write(cont)
      else :
             pass

file2 = open('c:/Users/Admin/Desktop/Python L1/Operation on a file P-1.Project/so.txt','r')
cont1 = file1.read()

print(cont1)

file1.close()
file2.close()


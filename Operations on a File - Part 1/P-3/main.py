file1 = open('c:/Users/Admin/Desktop/Python L1/Operations on a File - Part 1/P-3/Hi.txt','r')
file2 = open('c:/Users/Admin/Desktop/Python L1/Operations on a File - Part 1/P-3/Hello.txt','w')

for file in file1.readlines():

         if not (file.startswith('F1')):

                 print(file)

                 file2.write(file)


file2.close()
file1.close()
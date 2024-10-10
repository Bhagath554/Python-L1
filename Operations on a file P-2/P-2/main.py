#new_file = (' c:/Users/Admin/Desktop/Python L1/Operations on a file P-2/P-2/main.py/Hello.txt','x')
#new_file.close()

import os
print("Checking if any file is existing or not")
if os.path.exists('Hi.txt'):
 os.remove('Hi.txt')

else :
    print("The file does not exist")

my_file = open('Hi.txt','w')
my_file.write("Hello My Name is Bhagath")
my_file.close()

os.remove('Bye.txt')


with open('Hi.txt','w') as file:
    file.write("Hello My Name is Bhagath.")
file.close()

with open('Hi.txt','r') as file:
    data = file.readlines()
    print("Words in the Files are")
    for line in data :
     word = line.split()
     print(word)
file.close()
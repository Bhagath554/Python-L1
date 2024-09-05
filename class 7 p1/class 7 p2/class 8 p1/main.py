my_tuple = ()
print(my_tuple)

my_tuple = ("A","B","D")
print(my_tuple)

my_tuple = (1,"Hello","A")
print(my_tuple)

my_tuple = ("Hello",(1,3,5),[2,4,6])
print(my_tuple)

my_tuple = ("A","H","B","G","T")
print(my_tuple[2])
print(my_tuple[3])

n_tuple = ("Hello",(1,3,5),[2,4,6])
print(n_tuple[0][4])
print(n_tuple[0][1])

print("Sliced:",my_tuple[1:4+1])

for letter in (my_tuple):
    print("Hello",letter)

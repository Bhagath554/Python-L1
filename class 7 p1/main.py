list = ['Apple','Guava','Orange','Mango','']

print("Length of List:", len(list))
print("First Element:", list[0])
print("First Element:", list[-1])


list.remove("Apple")
print("Updated list :", list)

list.sort()
print("Sorted List :", list)

list.pop(3)
print("Updated List", list)

list.reverse()
print("Reversed List :", list)

print("Multiplication on list :",list*2)

list = list[:4]

print("SlicedList :" , list)

list.clear()
print("Cleared List: " , list)



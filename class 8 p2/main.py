my_Set = {1,2,3,3,4,5,5,5,9}
print("Set:",my_Set)

my_Set.add(5)
print("Updated Set:",my_Set)

set1 = (my_Set)
set2 = ("1","2","4","4")

print("\n Set 1,set1")
print("\nSet 2,set2")
print("Difference")
print(set1.difference(set2))
print("Symmetric Difference")
print(set1.symmetric_difference(set2))



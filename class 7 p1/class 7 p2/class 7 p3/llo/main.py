def test(lst):
    result = {}
    for item in lst :
      result[item[0]] = item[1:] 
    return  result

students = [[1, 'Bhagath', '6'], [2,'Arjun','6'], [3,'Tanush','7']]

print("/nOriginal list ")

print(students)
print("n/Converted list ")

print(test(students))
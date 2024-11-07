number = int(input("Enter a Number:"))
org_no = number
reversed_no = 0

while number >0:
    digit = number % 10
    reversed_no = reversed_no * 10  + digit
    number //= 10

if org_no == reversed_no :
    print(f"{org_no} is a palindrom")

else :
    print(f"{org_no} is not a palindrom")
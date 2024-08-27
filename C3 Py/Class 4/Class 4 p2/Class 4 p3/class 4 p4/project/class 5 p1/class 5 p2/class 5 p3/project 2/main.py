


name = (input("Name:"))
Class = (input("Class:"))
section = (input("Section:"))

Days = (input("Total Number of Working Days"))

if Days == 0:
    print("Error,Please Enter your No. Working Days or else you will be Suspended from the School")
Day = (input("Total Number of Days for Absent"))



if Day == 0:
    print("Error,Please Enter your No. of Days of absent or else you will be Suspended from the School")


result = Days / 150 * 100
print(f"The No. of working days of {name} is {Days} and the Percentage is {result}")

if result < 75 :
    print('You are not eligible to write the exam')

else :
    print("congrats {name} from {Class} & section {Section} is Your Are  Eligible to Write the Exam")

     




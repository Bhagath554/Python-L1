class Calculator:

      

      def __init__(self,num1,num2,num3):
    
    
       self.num1 = num1
       self.num2 = num2
       self.num3 = num3

    

    

      def addition(self):
       return self.num1 + self.num2 + self.num3

      def subtraction(self):
        return self.num1 - self.num2 - self.num3
      def product(self):
        return self.num1 * self.num2 * self.num3

      def average(self):
        return self.sum() / 2

num1 = int(input("Enter 1st no."))

num2 = int(input("Enter 2nd no."))

num3 = int(input("Enter 3rd no."))
c = Calculator(num1,num2,num3)
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
user_choice = input()

if user_choice not in ["1","2","3","4"]:
       print("Please enter a valid option")
       
else:
    user_choice = int(user_choice)
    

if user_choice == 1:
 total_sum = c.addition()
 print(f"Sum: {total_sum}")

elif user_choice == 2:
 total_sub = c.subtraction()
 print(f"subtracton: {total_sub}")

elif user_choice == 3:
 total_mul = c.multiplication()
 print(f"Product: {total_mul}")

elif user_choice == 4:
 total_div = c.average()
 print(f"Average: {total_div}")



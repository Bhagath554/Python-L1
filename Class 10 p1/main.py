class Employee:
       def _init_(self):
              print("Employee Created")

       def _del_(self):
                print("Destructor called,Employee Deleted")

obj = Employee()
del obj
          
class Person(object):

    def __init__(self,name,idnumber):
      self.name = name
      self.idnumber = idnumber

    def display(self):
                    print(self.name)
                    print(self.idnumber)

class employee(Person):
    def __init__(self,name,idnumber,salary,post):
                       self.salary = salary
                       self.post = post


                       Person.__init__(self,name,idnumber)

a = employee('penguin',200987,78668,"intern")                  
a.display()   


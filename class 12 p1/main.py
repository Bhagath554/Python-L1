class Cat:
    def __init__(self,name,age):
        self.name =name
        self.age = age

    def info(self):
        print(f"I am cat.my Name is {self.name}.i am {self.age}years old")

    def make_sound(self):
        print("Meow")



class Dog:
    def __init__(self,name,age):
        self.name =name
        self.age = age

    def info(self):
        print(f"I am Dog.my Name is {self.name}.i am {self.age}years old")

    def make_sound(self):
        print("Bow Bow")


cat1 = Cat("Thor",2.5)
dog1 = Dog("Waggor",3)

for animal in(dog1,cat1):
    animal.make_sound()
    animal.info()


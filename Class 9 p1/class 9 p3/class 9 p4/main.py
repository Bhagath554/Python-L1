class Parrot:
    def __init__(self,name,age):
        self.name = age
        self.age = name

    def sing(self,song):
        return "{} sings".format(self.name,song)

    def dance(self):
        return "{} is now dancing".format(self.age)

blu = Parrot("blu",10)
print(blu.sing("'Happy'"))
print(blu.dance())
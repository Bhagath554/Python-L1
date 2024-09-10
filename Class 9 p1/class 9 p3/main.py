class parrot:
    species = "Bird"

    def __int__(self,name,age):
        self.name = name
        self.age = age

blu = parrot("blu",10)
woo = parrot("woo",15)

print("blu is a{}".format(blu.species) )
print("woo is a{}".format(woo.species) )

print("{}is a{} years old".format(blu.name))
print("{}is a{} years old".format(woo.name))
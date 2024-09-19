class Square:

    def __init__(self):
        self._side = 10

    def area(self):
        print("Side is:",self._side)
        print("Area is:",self._side**2)

ob = Square()

ob._side = 15

ob.area()
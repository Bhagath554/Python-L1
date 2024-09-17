from abc import ABC
class Animal(ABC):

    def move(ABC):
        pass

   

class Snake(Animal):
   def move(ABC):
      print("I Can Crawl")

class Lion(Animal):
    def move(ABC):
      print("I Can Roar")




R = Snake()
R.move()

R = Lion()
R.move()



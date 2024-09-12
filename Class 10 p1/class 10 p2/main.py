class Library:

   def __init__(self,list,name):
    self.bookslist = list
    self.name = name
    self.dict = {}

    def displaybooks(self):
     print("We have the following books in Library:{self.name}")
       
     for book in self.bookslist: 
        print(book)

    def lendbook(self,user,book):
        if book  not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender book database has been Updated.You can take the book now")
        else :
                print(f"Book is Alred=ady is being used by others{self.lendDict[book]}")

    def addbook(self,book):
        self.booklist.append(book)
        print("The Book has been added to the library")

    def returnbook(self,book):
            self.lendDict.pop(book)
        
if __name__ == '__main__':
        books = Library(["Harry potter","Itachi Uchiha The dark Knight","Jujutsu Kaisen","Solo Leveling","Naruto","Naruto Sippuden"],"Demon Slayer")

        while(True):
            print(f"Welcome to the {books.name} library.Entr your Choice to Continue")

            print("1.Display Books")
            print("2.Lend a Book")
            print("3.Add a Book")
            print("4.Return a book")
            user_choice = input()

            if user_choice not in ["1,","2","3","4"]:
             print("Please enter a valid option")
             continue
            else:
                user_choice = int(input(user_choice))



            if user_choice == 1:
                books.displaybooks()
               

            elif user_choice == 2:
                    book = input("Enter the name of the book you want")
                    user= input("Enter the name")
                    books.lendbook(user,book)

            elif user_choice == 3:
                     book = input("Enter the name of the book you want to add")
                     books.addbook(user,book)

            elif user_choice ==4:
                        book= input("Enter the name of the book you want to Return")
                        books.returnbook(user,book)

            else:
                            print("Not a Valid Number")
                            print("")


                     
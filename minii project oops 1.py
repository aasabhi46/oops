class library:
    def __init__(self,list,name):
        self.booklist = list
        self.name = name
        self.lendDict = {}

    def displaybooks(self):
        print(f"we have following book in ours library:{self.name}")
        for book in self.booklist:
            print(book)
    def lendbook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book: user})
            print("lender book data have upadted. you can tak e from here")
        else:
            print(f"book is already used by {self.lendDict[book]}")
    def addbook(self, book):
        self.booklist.append(book)
        print("book has been added to the book list")

    def returnbook(self ,book):
        self.booklist.remove(book)

if __name__ == "__main__":
    harry = library(["Python", "java book" ,"love you the way you love me", "wings fire"] , "code with harry")

    while(True):
        print(f"welcome to the {harry.name} library. entere your choice to continue")
        print("1.display book")
        print("2. lend a book")
        print("3. add a book")
        print("4. return a book")
        User_choice = int(input())

        if User_choice==1:
            harry.displaybooks()

        elif User_choice == 2:
            book = input("enter the book you want to lend")
            user = input("enter your name")
            harry.lendbook(user, book)

        elif User_choice == 3:
            book = input("enter the book you want to add")
            harry.addbook(book)

        elif User_choice == 4:
            book = input("enter the book you return:")
            harry.returnbook(book)

        else:
            print("not a valid option")

        print("Press q to quit and c to continue")
        user_choice2 = " "
        while (user_choice2 != "c" and user_choice2 !='q'):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()

        if user_choice2 =="c":
            continue

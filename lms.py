class library:
    def __init__(self,books):
        self.books=books
        
    def avlbooks(self):
        for i in self.books:
            print(f"# {i}")
        print()

    def borrowbook(self):
        book=input("enter the book name you want to borrow: ")
        print()
        if book in self.books:
            print("the book has been issued to u\n")
            self.books.remove(book)
        else:
            print("sorry the book has been issued to someone else or not available\n")

    def returnbook(self):
        book=input("enter the bookname u want to return or donate: ")
        self.books.append(book)
        print("thank you for returning the book\n")
lms=library(["django","flask","python","uiux","html","css"])
while True:
    print('''Hey there Welcome to my Library
    
Select any option from below:
1:for getting avl books list
2:for borrowing book
3:for returning book
4:to exit''')    
    try:    
        a=int(input("enter any option: "))
        if a==1:
            lms.avlbooks()
        elif a==2:
            lms.borrowbook()
        elif a==3:
            lms.returnbook()
        elif a==4:
            exit()
        else:
            print("please choose from the option above")
    except Exception as e:
        print("Your input value can't be taken, Please enter a valid integer")

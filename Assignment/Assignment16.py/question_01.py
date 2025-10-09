class Book:
    count = 0 

    # Constructor
    def __init__(self, bid=102, bname= "One Part Women", price= 600, authour= "Perumal murugan"):
        Book.count += 1
        self.id = bid
        self.name = bname
        self.bprice = price
        self.bauthour = authour

    # Destructor
    def __del__(self):
        print(f"Destructure is called for {self.name}")
    
    # showBook 
    def showBook(self):
        print("_____Book Details_____")
        print("Book Id :", self.id)
        print("Book Name :", self.name)
        print("Book Price :", self.bprice)
        print("Book Authour :", self.bauthour)
    

    @staticmethod
    def totalBook():
        print(f"Total Book count is: {Book.count}")

# Parameterless Constructor
b1 = Book()
b1.showBook()


# Parameterized Constructor
b1 = Book(101, "HARUKI MURAKAMI", 500, "Jay rubin")
b1.showBook()


b1.totalBook()



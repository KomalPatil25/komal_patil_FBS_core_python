class Book:
    def __init__(self, bid=102, bname= "One Part Women", price= 600, authour= "Perumal murugan"):
        self.id = bid
        self.name = bname
        self.bprice = price
        self.bauthour = authour

    def showData(self):
        print("_____Book Details_____")
        print("Book Id :", self.id)
        print("Book Name :", self.name)
        print("Book Price :", self.bprice)
        print("Book Authour :", self.bauthour)
    
    def __del__(self):
        print("Destructure is called.")

b1 = Book(101, "HARUKI MURAKAMI", 500, "Jay rubin")
b1.showData()
# del b1
print()
b2 = Book()
b2.showData()
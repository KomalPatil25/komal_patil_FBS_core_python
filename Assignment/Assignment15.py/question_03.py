class Shirt:
    def __init__(self, sid=123, sname="Casual Shirt", type="cotton", price=1500, size="M"):
        self.id = sid
        self.name = sname
        self.stype = type
        self.sprice = price
        self.ssize = size

    def showShirt(self):
        print("_____Shirt detail_____")
        print("Shirt Id :", self.id)
        print("Shirt Name :", self.name)
        print("Shirt Type :", self.stype)
        print("Shirt Price :", self.sprice)
        print("Shirt Size :", self.ssize)

    def __del__(self):
        print("Destructure is called.")

# Parameterized
s1 = Shirt(123, "Classic White Shirt", "Formal", 2000, "L")
s1.showShirt()

# Parameterless
s2 = Shirt()
s2.showShirt()

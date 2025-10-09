class Shirt:
    # Static method
    shirt_price_change = {
        "small" : 0,
        "medium" : 0.1,
        "large" : 0.2,
        "xlarge" : 0.3
    }

    def __init__(self, sid=123, sname="Casual Shirt", type="cotton", price=1500, size="medium"):
        self.id = sid
        self.name = sname
        self.stype = type
        self.sprice = price
        self.ssize = size
    
    # Destructor is called
    def __del__(self):
        print("Shirt object destroyed!!!!!!!!!!")

    # showShirt Details
    def showShirt(self):
        if(self.ssize == "small"):
            final_price = self.sprice

        elif(self.ssize == "medium"):
            final_price = self.sprice + self.sprice * 0.1 #fp = self.price * (1 + 0.1)

        elif(self.ssize == "large"):
            final_price = self.sprice + self.sprice * 0.2

        elif(self.ssize == "xlarge"):
            final_price = self.sprice + self.sprice * 0.3

        else:
            final_price = self.sprice

        print("_____Shirt detail_____")
        print("Shirt ID :", self.id)
        print("Shirt Name :", self.name)
        print("Shirt Type :", self.stype)
        print("Shirt Price :", self.sprice)
        print("Shirt Size :", self.ssize)
        print("Shirt Price:", final_price)
        print("-------------------------------------")

# Parameterless
s = Shirt()
s.showShirt()
    
# Parameterized
s1 = Shirt(101, "Classic White Shirt", "Formal", 1000, "Small")
s1.showShirt()

s2 = Shirt(102, "Classic Black Shirt", "Formal", 1000, "medium")
s2.showShirt()

s3 = Shirt(103, "Classic Brown Shirt", "Formal", 1000, "large")
s3.showShirt()

s4 = Shirt(104, "Classic Sky blue Shirt", "Formal", 1000, "xlarge")
s4.showShirt()

s5 = Shirt(105, "Classic Red Shirt", "Formal", 1000, "Small")
s5.showShirt()


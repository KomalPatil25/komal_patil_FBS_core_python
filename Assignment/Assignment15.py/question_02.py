class Product:
    def __init__(self,pid="@52", pname="Runining Shoes", price="3500", quality="Durable"):
        self.id = pid
        self.name = pname
        self.p = price
        self.q = quality

    def showProduct(self):
        print("_____Product Details_____")
        print("Product Id :", self.id)
        print("Product Name :", self.name)
        print("Product Price :", self.p)
        print("Product Quality :", self.q)

    def __del__(self):
        print("Destructure is called.")

# Parameterized
p1 = Product("@273", "Wireless Headphones", "5000", "Exellent")
p1.showProduct()

# Parameterless
p2 = Product()
p2.showProduct()
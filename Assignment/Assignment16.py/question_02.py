class Product:
    discount = 0.1 # 10% discount

    # Constructor
    def __init__(self, pid=101, pname="Dairy Milk", price=100, quantity=500):
        self.id = pid
        self.name = pname
        self.price = price
        self.quantity = quantity
    
    # Destructor
    def __del__(self):
        print(f"Destructor called for Product {self.name}")

    # showProduct details
    def showProduct(self):
        print("_____Product Details_____")
        return f"ID:{self.id}\nPRODUCT NAME:{self.name}\nPRICE:{self.price}\nQUANTITY:{self.quantity}\nPRODUCT DISCOUNT:{Product.discount * 100}%"
    
    # calculate discount
    def calcDiscount(self):
      total_price = self.price * self.quantity
      discount_amount = total_price * Product.discount
      return discount_amount
       
    
    @staticmethod
    def calculateDiscount(price, quantity):
        total_price = price * quantity
        discount_amount = total_price * Product.discount
        return total_price - discount_amount
    
# Parameterless Constructor
p1 = Product()
print(p1.showProduct())
p1.calcDiscount()

# Parameterized Constructor
p1 = Product(101, "kitkat", 1000, 5)
print(p1.showProduct())
p1.calcDiscount()
print("Total after discount: ", Product.calculateDiscount(1000, 5))
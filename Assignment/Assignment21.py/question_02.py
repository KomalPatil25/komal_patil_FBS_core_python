class Television:
    def __init__(self):
        self.model_number = 0
        self.screen_size = 0
        self.price = 0.0

    def grt_data(self):
        try:
            self.model_number = int(input("Enter the model number: "))
            self.screen_size = int(input("Enter the screen size: "))
            self.price = float(input("enter the price: "))

            if len(str(self.model_number)) > 4:
                raise ValueError('Model number can not have more than four digit.')
            
            if self.screen_size < 12 or self.screen_size > 70:
                raise ValueError('Screen size must be between 12 and 70 inches.')
            
            if self.price < 0 or self.price > 5000:
                raise ValueError('Price must be between Rs.0 and Rs.5000.')
            
        except Exception as e:
            print('ERROR: ', e)
            print('Resetting all values to zero....')
            self.model_number = 0
            self.screen_size = 0
            self.price = 0

    def display(self):
        print(f'Model Number: {self.model_number}\nScreen Size: {self.screen_size}\nPrice: Rs.{self.price}')

if __name__ == '__main__':
    obj = Television()
    obj.grt_data()
    obj.display()
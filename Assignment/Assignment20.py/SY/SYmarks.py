class SYMARKS:
    def __init__(self, Computer_Total, Maths_Total, Electronics_Total):
        self.ct = Computer_Total
        self.mt = Maths_Total
        self.et = Electronics_Total

    def display(self):
        return f'SY MARKS : Computer Total: {self.ct}, Maths Total: {self.mt}, Electronic Total: {self.et}'
        
    # def total_marks(self):
    #     return self.ct + self.mt + self.et
        
# obj = SYMARKS(88, 72, 80)
# print(obj)
# print('Total Marks: ', obj.total_marks())
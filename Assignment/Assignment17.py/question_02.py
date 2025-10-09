from question_01 import Student

class EnggStudent(Student):
    def __init__(self, roll_no=1, name="Komal", age=19, percentage=91, branch="Compuer_Science", internalmarks=85):
        super().__init__(roll_no, name, age, percentage)
        self.branch = branch
        self.intmarks = internalmarks

    def displayData(self):
        super().displayData()
        print(f"BRANCH : {self.branch}")
        print(f"INTERNAL MARKS : {self.intmarks}")

    def accept(self):
        print("_____ENGINEERING STUDENT DETAILS_____")
        super().accept()
        self.branch = input("Enter the branch: ")
        self.intmarks = int(input("Enter internal marks: "))
        
    def calcRank(self):
        final_score = self.sper +(self.intmarks / 2)
        if(final_score >= 120):
            print("A+")
            # print(final_score)
        
        elif(final_score >= 100):
            print("A")

        elif(final_score >= 80):
            print("B")

        else:
            print("C")

    def __str__(self):
        return f"ROLL NO : {self.srl}\nNAME : {self.snm}\nAGE : {self.sage}\nPERCENTAGE : {self.sper}\nBRANCH : {self.branch}\nINTERNAL MARKS : {self.intmarks}"


# es1 = EnggStudent()
# es1.accept()
# es1.displayData()
# es1.calcRank()
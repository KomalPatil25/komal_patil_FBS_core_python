from question_01 import Student

class MedicalStudent(Student):
    def __init__(self, roll_no=1, name="Komal", age=19, percentage=91, specialization="Cardiology", marksofinternship=500):
        super().__init__(roll_no, name, age, percentage)
        self.speci = specialization
        self.internshipmark = marksofinternship

    def displayData(self):
        super().displayData()
        print(f"SPECIALIZATION : {self.speci}")
        print(f"MARKS OF INTERNSHIP : {self.internshipmark}")

    def accept(self):
        print("_____MEDICAL STUDENT DETAIL_____")
        super().accept()
        self.speci = input("Enter the specialization: ")
        self.internshipmark = int(input("Enter the internship marks: "))

    def calcRank(self):
        final_score = self.sper +(self.internshipmark / 2)
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
        return f"ROLL NO : {self.srl}\nNAME : {self.snm}\nAGE : {self.sage}\nPERCENTAGE : {self.sper}\nSPECIALIZATION : {self.speci}\nMARKS OF INTERNSHIP : {self.internshipmark}"

ms1 = MedicalStudent()
ms1.accept()
ms1.displayData()
ms1.calcRank()


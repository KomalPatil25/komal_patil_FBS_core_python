# class Student:
#     def __init__(self, id=1, name="Komal", age=19, marks=456, percentage=91):
#         self.sid = id
#         self.snm = name
#         self.sage = age
#         self.smark = marks
#         self.sper = percentage
        
#     def accept(self):
#         print("_____Student Details_____")
#         self.sid = input("Enter student id: ")
#         self.snm = input("Enter student name: ")
#         self.sage = input("Enter student age: ")
#         # self.smark = input("Enter student total gain marks: ")
#         # self.sper = int(input("Enter student percentage: "))


#     def calMarks(self):
#         total = 0
#         print("Enter marks of five subjects: ")
#         for i in range(5):
#             marks = int(input(f"Subject {i + 1}: "))
#             total += marks
#         print("Total marks: ", total)
#         self.sper = (total / 500) * 100
    
#     def displayData(self):
#         print(f"ID : {self.sid}")
#         print(f"NAME : {self.snm}")
#         print(f"AGE : {self.sage}")
#         print(f"Total Marks: {self.smark}")
#         print(f"PERCENTAGE : {self.sper}")

#     def rankDisplay(self):
#         if(self.sper >= 90 and self.sper <= 100):
#             print("Grade A")
#         elif(self.sper >= 70 and self.sper <= 90):
#             print("Grade B")
#         elif(self.sper >= 50 and self.sper <= 70):
#             print("Grade C")
#         elif(self.sper >= 30 and self.sper <= 50):
#             print("Grade D")
#         elif(self.sper >= 1 and self.spr <= 30):
#             print("Pass")
#         else:
#             print("Invalid percentage.")

# s1 = Student()
# s1.accept()
# s1.calMarks()
# s1.displayData()
# s1.rankDisplay()



class Student:
    def __init__(self, roll_no=1, name="Komal", age=19, marks=456, percentage=91):
        self.srl = roll_no
        self.snm = name
        self.sage = age
        self.smark = marks
        self.sper = percentage
        
    def accept(self):
        print("_____Student Details_____")
        self.sid = input("Enter student roll no: ")
        self.snm = input("Enter student name: ")
        self.sage = input("Enter student age: ")
        self.smark = int(input("Enter student total gain marks: "))
        # self.sper = int(input("Enter student percentage: "))


    def calMarks(self):
        total = self.smark
        self.sper = (total / 500) * 100
    
    def displayData(self):
        print(f"ROLL NO : {self.srl}")
        print(f"NAME : {self.snm}")
        print(f"AGE : {self.sage}")
        print(f"TOTAL MARKS: {self.smark}")
        print(f"PERCENTAGE : {self.sper}")

    def rankDisplay(self):
        if(self.sper >= 90 and self.sper <= 100):
            print("Grade A")
        elif(self.sper >= 70 and self.sper <= 90):
            print("Grade B")
        elif(self.sper >= 50 and self.sper <= 70):
            print("Grade C")
        elif(self.sper >= 30 and self.sper <= 50):
            print("Grade D")
        elif(self.sper >= 1 and self.sper <= 30):
            print("Pass")
        else:
            print("Invalid percentage.")

    def __str__(self):
        return f"ROLL NO : {self.srl}\nNAME : {self.snm}\nAGE : {self.sage}\nTOTAL MARKS: {self.smark}\nPERCENTAGE : {self.sper}"

# s1 = Student()
# s1.accept()
# s1.calMarks()
# s1.displayData()
# s1.rankDisplay()
# print(s1)

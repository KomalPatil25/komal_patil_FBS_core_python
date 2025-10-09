class College:
    def __init__(self, num_students):
       self.students = []
       self.capacity = num_students

    def addStudent(self, roll_no, name, age, marks):
        if(len(self.students) < (self.capacity)):
            for i in self.students:
                if(i["roll_no"] == roll_no):
                    print(f"Student with this {roll_no} already exists.")
            return self.students.append({f"Roll No:{roll_no}, Name:{name}, Age:{age}, marks:{marks}"})
            print(f"Student:{name} added successfully")
        else:
            print(f"can not add Student")

    def getStudent(self, roll_no):
        for i in self.students:
            if(i["roll_no"] == roll_no):
                return i
        return None

    def removeStudent(self, roll_no):
        for i in self.students:
            if i["roll_no" == roll_no]:
                self.students.remove(i)
                print(f"Student {i['name']} remove successfully")
        return print("Student not found")


c1 = College(3)
c1.addStudent(27, "Komal", 19, 98)
c1.addStudent(28, "Rutika", 20, 99)
c1.addStudent(34, "Priya", 21, 87)
print(c1.getStudent(1))


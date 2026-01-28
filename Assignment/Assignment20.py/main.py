from SY.SYmarks import SYMARKS
from TY.TYmarks import TYMARKS

class Student:
    def __init__(self, roll_no, name, sy_marks, ty_marks):
        self.roll_no = roll_no
        self.name = name
        self.sy_marks = sy_marks
        self.ty_marks = ty_marks

    def calc_result(self):
        total = self.sy_marks.ct + self.ty_marks.theory
        avg = total / 2

        if avg >= 70:
            grade = 'A'
        elif avg >= 60:
            grade = 'B'
        elif avg >= 50:
            grade = 'C'
        elif avg >= 40:
            grade = 'Pass Class'
        else:
            grade = 'Fail'

        return total, avg, grade
    
    def display(self):
        print(f'Roll No: {self.roll_no}\nName: {self.name}')
        self.sy_marks.display()
        self.ty_marks.display()

        total, avg, grade = self.calc_result()
        print(f'Total (Computer + Theory): {total}')
        print(f'Averege: {avg}')
        print(f'Grade: {grade}')

if __name__ == '__main__':
    sy = SYMARKS(80, 75, 70)
    ty = TYMARKS(85, 90)

    st = Student(roll_no=101, name='komal',sy_marks=sy, ty_marks=ty)
    st.display()
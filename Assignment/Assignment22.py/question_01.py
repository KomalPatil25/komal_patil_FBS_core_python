import pickle

emp_file = 'Core_Python/Assignment/Assignment22.py/emp.txt'
class Emp:
    def __init__(self, eid=101, ename='Komal', basic=550000):
        # self.emp_file = 'Core_Python/Assignment/Assignment22.py/emp.txt'
        self.eid = eid
        self.ename = ename
        self.basic = basic

    def __str__(self):
        return f'Employe ID: {self.eid}, Name: {self.ename}, Basic: {self.basic}'

    def add_record(self):
        print('--------- ADD RECORD ---------')
        try:
            eid = input('Enter Employee ID: ')
            ename = input('Enter Employee Name: ')
            basic = input('Enter Basic Salary: ')
            emp = Emp(eid, ename, basic)
            with open(emp_file, 'ab') as f:
                pickle.dump(emp, f)
                f.write('\n',)
            print('Record added successfully!')
        except Exception as e:
            print('ERROR: ', e)

    def search_record(self):
        print('-------- SEARCH RECORD --------')
        eid = input('Enter Employee ID to Search: ')
        try:
            with open(emp_file, 'rb') as f:
                emp = pickle.load(f)
                if emp.eid == eid:
                    print('Record Found.')
                    emp.display()
                else:
                    print('Record not Found.')
        except Exception as e:
            print('ERROR: ', e)
                    
    def delete_record(self):
        print('-------- DELETE RECORD --------')
        try:
            eid = input('Enter Employe Id to delete: ')
            chk = False
            employees = []
            with open(emp_file, 'rb') as f:
                emp = pickle.load(f)
                employees.append(emp)

            with open(emp_file, 'wb') as f:
                for emp in employees:
                    if emp.eid != eid:
                        pickle.dump(emp, f)
                        chk = True
            if chk:
                print('Record deleted successfully.')
            else:
                print('Record is not found.')
        except Exception as e:
            print('ERROR: ', e)

    def edit_record(self):
        print('--------- EDIT RECORD --------')
        try:
            eid = input('Enter Employe Id to delete: ')
            chk = False
            employees = []
            with open(emp_file, 'rb') as f:
                emp = pickle.load(f)
                employees.append(emp)

            with open(emp_file, 'wb') as f:
                for emp in employees:
                    if emp.eid == eid:
                        print('Record found! Enter new credentials: ')
                        emp.name = input('Enter Employee Name: ')
                        emp.basic = input('Enter Basic Salary: ')
                        pickle.dump(emp, f)
                        chk = True

            if chk:
                print('Record update successfully.')
            else:
                print('Record not found.')

        except Exception as e:
            print('ERROR: ', e)

    def display_all_record(self):
        print('-------- DISPLAY ALL RECORD --------')
        try:
            with open(emp_file, 'rb') as f:
                emp = pickle.load(f)
                emp.display()

        except Exception as e:
            print('ERROR: ', e)

    def main(self):
        while True:
            print('======== EMPLOYEE MANAGEMENT SYSTEM ========')
            print('''Select Opetion Below: 
                  1. Add Record.
                  2. Search Record.
                  3. Delete Record.
                  4. Edit Record.
                  5. Display All Records.
                  6. Exit.''')
            
            ch = input('Enter your choice(1-6): ')

            if ch == '1':
                self.add_record()
            elif ch == '2':
                self.search_record()
            elif ch == '3':
                self.delete_record()
            elif ch == '4':
                self.edit_record()
            elif ch == '5':
                self.display_all_record()
            elif ch == '6':
                print('Exiting program...')
                break
            else:
                print('Invalid choice. Please try again.')

if __name__ == '__main__':
    obj = Emp()
    obj.main()
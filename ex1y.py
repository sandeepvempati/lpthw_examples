class Employee:

    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self,fname,lname,salary): # constructor or intialising
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.email = fname + '.' + lname + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return ('{} {}'.format(self.fname,self.lname))

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)

    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = aount


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, fname, lname, salary, prog_lang):
        #super().__init__(self,fname, lname, salary)
        Employee.__init__(self,fname, lname, salary)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, fname, lname, salary, employees=None):
        Employee.__init__(self, fname, lname, salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print ("--->>>" ,emp.fname)



emp1 = Developer('syud', 'vinay', 50000, 'python')
emp2 = Developer("dan", "ikel", 60000, 'java')
mgr1 = Manager("sandeep","vempati", 90000,[emp2])
print mgr1.email
#mgr1.add_emp(emp1)
mgr1.remove_emp(emp2)
mgr1.print_emps()
#print(isinstance(mgr1,Developer))
print (issubclass(Manager, Employee))

# emp_str_1 = 'john-doe-8000'
# fname,lname,salary = emp_str_1.split('-')
# new_emp1 = Employee(fname,lname,salary)
# print emp1.prog_lang
# print emp2.prog_lang
#
# print emp1.salary
# emp1.apply_raise()
# print emp1.salary
# print emp2.email



# Employee.set_raise_amount(1.05)
# emp1.set_raise_amount(1.08)
# print(Employee.raise_amount)
# print(emp1.raise_amount)
# print(emp2.raise_amount)
# Employee.raise_amount = 1.05 #it changes at class level
# emp1.raise_amount  = 1.10 #it adds attribute to employee1 instance
# print (emp2.salary)
# emp2.apply_raise()
# print (emp2.salary)
# print(emp1.salary)
# emp1.apply_raise()
# print (emp1.salary)
#
# print (emp1.__dict__)
# print (emp2.__dict__)
# print (Employee.__dict__)
#
# print Employee.num_of_emps

class Employee:

    empCount = 0
    def __init__(self, name, salary):
        self.name = name;
        self.salary = salary;
        Employee.empCount +=1;

    def displayCount(self):
        print("d")

    def displayEmployee(self):
        print(f"Name: {self.name} Salary: {self.salary}")


emp1 = Employee("Zara", 2000)
#emp1.displayEmployee()
emp1 = Employee("Mehedi", 2500)
#emp1.displayEmployee()

emp1.age = 70;

emp1.age = 90;



#del emp1.age;
##print("Total Employee",Employee.empCount, emp1.age, getattr(emp1, 'age'), setattr(emp1, 'age', 800), getattr(emp1, 'age'))
print("Employee.__doc__:", Employee.__doc__)

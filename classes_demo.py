
class Employees:

    emp=0

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employees.emp+=1

    def displayC(self):
        print ("Total : ", Employees.emp)

    def displayE(self):
        print ("Name : ", self.name, "Salary : ", self.salary)



emp1=Employees("AZ", 1000)
emp2=Employees("SZ", 1000)

emp1.displayE()
emp2.displayE()

print ("Total Employee : ", Employees.emp)

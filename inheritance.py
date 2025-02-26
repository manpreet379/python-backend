class Employee:
    company="ITC"
    name="defauly"
    def show(self):
        print(f"The name of the employee is {self.name} and company is {self.company}")


class Code:
    language="cpp"
class Programmer(Employee,Code):
    company="ITC infotech"
    def showlang(self):
        print(f"The name is {self.name} and language is {self.language}" )


a=Employee()
b=Programmer()
a.name="manpreet"
a.salary="1200000"
a.show()
b.showlang()
#Employee.show(a)
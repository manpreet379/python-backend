#OOPS

class Employee:
    name="Manpreet"
    language="Py"
    salary=1200000
    
    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("Good morning")

    
    
manpreet=Employee()
print(manpreet.language)
manpreet.age=21
print(manpreet.age)
#here name lang, salary are class attributes while age is object attribute
# object attributes prefernce order is higher than class attributes
manpreet.language="cpp"
print(manpreet.language)
manpreet.getinfo()##this line is actually Employee.getinfo(manpreet) so if i dont write self /
                    ##this in cpp her it will say it takes 0 positonal arguments but one was given
Employee.getinfo(manpreet)
manpreet.greet()

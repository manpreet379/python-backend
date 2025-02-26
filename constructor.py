#OOPS

class Employee:
    name="Manpreet"
    language="Py"
    salary=1200000
    
    
    def __init__(self,salary,name,language):
        self.salary=salary
        self.name=name
        self.language=language
        print("Object created")
        
    
    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("Good morning")



manpreet=Employee(1200000,"manpreet","cpp")

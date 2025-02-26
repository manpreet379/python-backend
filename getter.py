class Employee:
    def __init__(self, name, salary):
        self._name = name  # Protected variable
        self._salary = salary

    @property
    def salary(self):  # Getter
        return self._salary

    @salary.setter
    def salary(self, amount):  # Setter
        if amount < 3000:
            raise ValueError("Salary cannot be less than 3000")
        self._salary = amount

e1 = Employee("John", 5000)
print(e1.salary)  # Output: 5000

e1.salary = 7000  # Valid update
print(e1.salary)  # Output: 7000

# e1.salary = 2000  # Raises ValueError: Salary cannot be less than 3000

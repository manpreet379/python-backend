#Operator overloading allows us to redefine the behavior of operators (+, -, *, /, etc.) for user-defined classes. In Python, this is achieved by overriding special methods (dunder methods) like __add__, __sub__, __mul__, etc.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # Overloading `+` operator
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):  # To print object
        return f"({self.x}, {self.y})"

p1 = Point(2, 3)
p2 = Point(4, 5)

result = p1 + p2  # Calls p1.__add__(p2)
print(result)  # Output: (6, 8)

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):  
        return self._name

    @name.setter
    def name(self, new_name):  # Setter for name
        print("Setting name...")
        if len(new_name) < 3:
            raise ValueError("Name must be at least 3 characters long!")
        self._name = new_name

p = Person("Alice")
p.name = "Bob"  # Calls setter
print(p.name)   # Calls getter
# Output:
# Setting name...
# Bob

# p.name = "Al"  # Raises ValueError

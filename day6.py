class Animal:
    
    def __init__(self,name):
        self.name=name
        
    
    def speak(self):
        print("Animal is speaking")
        
    def move(self):
        print("Animal moves")
        

class Dog(Animal):
    
    def __init__(self, name,breed):
        super().__init__(name)
        self.breed=breed
    
    def speak(self):
        print("Bow bow")
        
    @classmethod
    def animal_type(cls):
        print("Canine")
    
    
    
    @staticmethod
    def info():
        print('''Dogs, scientifically known as Canis lupus familiaris, 
are domesticated mammals that are a subspecies of the gray wolf (Canis lupus).
They are believed to have descended from wolves tens of thousands of years ago, making them one of the oldest domesticated animals.''')
        

    def move(self):
        print("Dog moves")
    def bark(self,volume="high"):
        print(f"Barking at {volume} volume")
    
    def tricks(self,*args):
        if args:
            print(f"{self.name} knows these tricks:")
            for trick in args:
                print(f"- {trick}")
        else:
            print(f"{self.name} doesn't know any tricks yet.")
        
#creating dog object
d=Dog("bruno","golden retriver")
a=Animal("golden retriver")
print(a.name)
#calling static method
Dog.info()

#method overload

d.tricks("roll")

#calling overriden method
d.speak()
def add_two_numbers():
    while True:
        try:
            a=int(input("Enter first number: "))
            b=int(input("Enter second number: "))
            print("The sum of two numbers is: ",a+b)
            break
        except ValueError:
            print("Give valid input")


       
    while True:
        try:
            age = int(input("Enter your age: "))
            if age < 13:
                print("You are a child.")
            elif 13 <= age <= 19:
                print("You are a teenager.")
            else:
                print("You are an adult.")
            break
        except ValueError:
            print("Please enter a valid age.")

    
    while True:
        try:
            num = int(input("Enter a number to check if it's positive, negative, or zero: "))
            if num > 0:
                print(f"{num} is a positive number.")
            elif num < 0:
                print(f"{num} is a negative number.")
            else:
                print(f"{num} is zero.")
            break
        except ValueError:
            print("Please enter a valid number.")

    
    while True:
        try:
            year = int(input("Enter a year to check if it's a leap year: "))
            if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
                print(f"{year} is a leap year.")
            else:
                print(f"{year} is not a leap year.")
            break
        except ValueError:
            print("Please enter a valid year.")

def exam_score():
    while True:
        try:
            sub1=int(input("Enter marks of subject1: "))
            sub2=int(input("Enter marks of subject2: "))
            break
        except ValueError:
            print("Give valid input")

    if(sub1<33):
        print("Failed in subject 1")
    elif(sub1>90):
        print("Pass with distinction in subject 1")
    else:
        print("Pass in subject 1")
    

    if(sub2<33):
        print("Failed in subject 2")
    elif(sub2>90):
        print("Pass with distinction in subject 2")
    else:
        print("Pass in subject 2")


def arthmeticoperations():
    while True:
        try:
            a=int(input("Enter first number: "))
            b=int(input("Enter second number: "))
            break
        except ValueError:
            print("Give valid input")

    print("The sum of two numbers is: ",a+b)
    print("The diff of two numbers is: ",a-b)
    print("The product of two numbers is: ",a*b)
    print("The division of two numbers is: ",a/b)
    print("The power of two numbers is: ",a**b)

    l1=[1,2,3,4,5,6]
    print(2 in l1)
    a=23
    b=23
    print(a is b)
    c="manpreet"
    d="manpreetsingh"
    print(c is d)
    print(a is not b)
    print(type(a))
    print(type(c))



add_two_numbers()

exam_score()

arthmeticoperations()
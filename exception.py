def divide(a,b):
    try:
        result=a/b
        return result
    except ZeroDivisionError as e:
        return "Cannot divide by zero try again "
       

n=int(input("Enter number:"))
a=int(input("Enter second number"))
if(a==0):
    raise ZeroDivisionError("cant divide by zero")
print(divide(2,5))
print(divide(5,0))
        

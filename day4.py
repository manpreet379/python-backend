
#functions
from functools import reduce
# task1 1
def even_numbers(lst):
    newlist=[]
    for num in lst:
        if(num%2==0):
            newlist.append(num)
    
    return newlist

a=int(input("Enter number of elemtns in list:"))
lst=[]
for i in range(a):
    b=int(input("Enter element: "))
    lst.append(b)
newl=even_numbers(lst)
print(newl)


#task2

def reverse_string(str):
    newstring=""
    for char in str:
        newstring=char+newstring

    print(newstring)
    
    # reversed_s = str[::-1]
    # print(reversed_s)  
str=input("Enter the string you want to reverse:")
reverse_string(str)

#lambda functions\
    
#task1 

a=int(input("Enter number of elemtns in list:"))
lst=[]
for i in range(a):
    b=int(input("Enter element: "))
    lst.append(b)
newlist2=filter(lambda x:x%2==1,lst)
for num in newlist2:
    print(num)

#task 2
print("Squares of list")
mysquare=lambda x:x*x
squared=map(mysquare,lst)
for num in squared:
    print(num,end=" ")
    
    
# map , reduce , filter

#map
print()
a=int(input("Enter number of elemtns in list:"))
lst=[]
for i in range(a):
    b=int(input("Enter element: "))
    lst.append(b)

newlist3=map(lambda x:x*2,lst)
print("Doubled list:")
for num in newlist3:
    print(num,end=" ")

# reduce
print()
a=int(input("Enter number of elemtns in list:"))
lst=[]
for i in range(a):
    b=int(input("Enter element: "))
    lst.append(b)
newlist4=reduce(lambda a,b:a*b,lst)

print("Product of list:")
print(newlist4)


# decorators

import time
def timer(func):
    def wrapper():
        before=time.time()
        func()
        print("Function took",time.time()-before,"seconds")
    return wrapper

@timer
def run():
    time.sleep(2)

run()


# execuriotn logger
def execution_logger(func):
    def wrapper(*args, **kwargs):
        print("Execution Started")
        result = func(*args, **kwargs)
        print("Execution Completed")
        return result
    return wrapper

@execution_logger
def greet(name):
    print(f"Hello, {name}!")

greet("Manpreet")

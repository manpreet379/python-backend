##walrus allows to assign values to varibales as part of expression :=
if(n:=len([1,2,3,4,5]))>3:
    print(f"List is too long {n} elements ,expected<=3")
    

# type expressions
    
#teeling what type of data type it is or what funtion is returning 
a:int=10

def sum(a:int,b:int)->int:#return type->int 
    return a+b

print(sum(a,5))
from typing import TypeAlias
vector:TypeAlias=list[float]

def scale(v1:vector,factor:float)->vector:
    return [x*factor for x in v1]
v1:vector=[1.0,2.0,3.0]
print(scale(v1,2))
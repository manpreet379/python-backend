def double(x):
    return x*2

doub=lambda x:x*2

print(double(5))
print(doub(5))
def appl(fx,value):
    return value+fx(value)

cube=lambda x:x*x*x
print(appl(cube,3))#passing function as argument

def cube(x):
    return x*x*x

l=[1,2,3,4,5]
newl=list(map(cube,l))
newl.sort(reverse=True)
for num in newl:
    print(num)
#filter
def filter_function(a):
    return a>4

newnewl=list(filter(filter_function,newl))
print(newnewl)


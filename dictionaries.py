marks={"manpreet":100,
        "dev":99,

       }
print(marks,type(marks))
print(marks["dev"])
for key in marks:
    print(key)

for key,value in marks.items():
    print(key,":",value)

print(marks.keys())
print(marks.values())
#dict.pop(key)
#dict.get(key,default) deafault if not found it does not give error but dict["key"] givs eroor if not found
#set no duplicates , dict no duplicate keys set in unordered
s={1,2,3}
print(type(s))
a=set()
print(type(a))
for i in range(0,8):
    n=int(input("Enter numbers :"))
    a.add(n)

print(a)
#lists are mutable while strings are not
friends=["Apple","Orange",5,6,345.06,False,"Aakash","Rohan"]
print(friends[0])
print(friends[4])
friends[0]="grapes"
print(friends[0])
#out of range print(friends[8])
#string return new value 
friends.append("manpreet")
print(friends)
l1=[1,5,2,6,4]
l1.sort()
print(l1)
#l1.insert(after ind,element)
#l1.pop(ind)
#l1.pop() pop from end
l1.remove(5)
print(l1)
#tuple is like list but it is immutable



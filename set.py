#set : not repitat elemants
a={1,2,3,4,1}
print(type(a))
print(a)
b={} # This is not empty set
print(type(b))

c= set() # This is empty set
print(type(c))

c.add(3)
c.add(3)
c.add(4)
c.add(5)
# c.add([1,2,3,4] )list can't add in set 
c.add((3,4,5,6))

print(c)
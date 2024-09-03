latter= '''Dear <|Name|>
you are so cute I am glade you got first prise in class
i am  happy 
you  are my best friend 
Date <|Date|>'''
Name=input('enter your name: ')
Date=input('enter Date: ')
latter=latter.replace('<|Name|>',Name)
latter=latter.replace('<|Date|>',Date)
print(latter)
#find double space
doubleSpaces=latter.find("  ")
print(doubleSpaces)

#replace doublespace with singel space
latter=latter.replace("  "," ")
print(latter)

print(latter[0])

a=[2,3,4,566,77]

print(a)

print(a[2])

a[0]=88
print(a)

friends=['misbah','maadeha','radia','liba']
print(friends[0:2])

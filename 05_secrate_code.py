import random
str = input("enter a string : ")
new_string=""
for i in range(len(str)):
    if i > 3:
        new_string= str[1:]+str[0]
        first= random.randint(chr(92),chr(122))
        
        
    else:
        new_string=str[::-1]
print(new_string)
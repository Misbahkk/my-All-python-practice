# This is a code of shifting the string by one encraption
# input: Misbah --> Output: Njtcbi
f= open("new.txt","w")
data=input("Enter the string: ")
string=""
for char in data:
    if (char==" "):
        string+=" "
    else:
        y= chr(ord(char)+1)
        string+=y
print(f" {string} : string is a encration of {data}",end="")
print(f" {string} : string is a encration of {data}",end="\n",file=f)
f.close()

# This is a code of shifting the string by one depcryption
# input: Misbah --> Output: Lhraai
f= open("new.txt","a")
data=input("\nEnter the string: ")
string=""
for char in data:
    if (char==" "):
        string+=" "
    else:
        y= chr(ord(char)-1)
        string+=y
print(f"{string}:  string is a Depcryption  of {data}",end="")
print(f"{string}: string is a Depcryption of {data}",end="\n",file=f)
f.close()
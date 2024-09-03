# sub1 = int(input("Enter 1st subject markx \n "))
# sub2 = int(input("Enter 2nd subject markx \n "))
# sub3 = int(input("Enter 3rd subject markx \n "))

# if(sub1<33 or sub2<33 or sub3<33):
#   print("Your fail becouse you get less then 33 markx in 1 subject: ")

# elif(sub1+sub2+sub3)/3 < 40:
#     print("You are fail : ")
# else:
#     ("Your pass!")



# Q2- check length are grater than 10

# name= input("Enter user name :")

# if(len(name)>10):
#     print("yes")
# else:
#     print("no")


#Q3 - name presnt in list

# List = [ "Misbah" , "Yousaf" , "Laiba" , "Kinza"]
# name = input("Enter name : ")

# if(name in List):
#     print("Name present in list")
# else:
#     print("NAme is not present in list")



#Q4 - markx with grade

markx = int(input("Enter markx : \n"))

if markx>=90:
    grade= "Ex"
elif markx>=80:
    grade ="A"
elif markx>=70:
    grade ="B"
elif markx>=60:
    grade ="C"
elif markx>=50:
    grade ="D"
else:
    grade="F"

print("Your grade is  --> "+grade )

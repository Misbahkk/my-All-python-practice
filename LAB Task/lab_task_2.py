# Q1 --> inter a 5 subject markx and calculate the persantage and agregate markx and grade
# -----------------------------------------------------------------------------------------
# obtain = 0
# for i in range(1,6):
#     markx = int(input("Enter a Markx: "))
#     print("Subject ",i,"markx is",markx)
#     obtain = obtain + markx
# percentage = obtain/500 *100
# print("Your percentage is: ",percentage)

# if percentage>=90:
#     grade= "Ex"
# elif percentage>=80:
#     grade ="A"
# elif percentage>=70:
#     grade ="B"
# elif percentage>=60:
#     grade ="C"
# elif percentage>=50:
#     grade ="D"
# else:
#     grade="F"

# print("Your grade is  --> "+grade )


# __________________________________________________________________________________
# __________________________________________________________________________________
# Q2 --> when we input alphabate , digit , special character 
# -----------------------------------------------------------
# character = input("Enter Any num ")
# if character>= 'a' and character<='z':
#     print("You enter Small Alphabate ")
# elif character>='A' and character<='Z':
#     print("You enter Capital Latter ")
# elif character>='0' and character<='9':
#     print("You enter Digit ")
# else:
#     print("You Enter Special Digit ")



# _____________________________________________________________________________________
# ______________________________________________________________________________________

# Q3 --> libarary membership
# --------------------------

# days = int(input("Enter a Days you return a book "))

# if days == 0:
#     print("you don't payany fine ")
# elif days <= 5:
#     print("Your fine is Rs.5")
# elif days <= 10:
#     print("Your fine is Rs.10")
# elif days <= 30:
#     print("Your fine is 25")
# elif days > 30:
#     print("You return book after 30 days , thats way Your membership is cancelled ")
    

# ____________________________________________________________________________________
# ____________________________________________________________________________________
# Q4 --> findleap year
# --------------------

# year = int(input("Enter a year "))
# if year % 4==0 or year % 100==0:
#     print(year," is a leap year")
# else:
#     print(year," is not a leap year")

# ________________________________________________________________________________________
# _________________________________________________________________________________________

# Q5-->chacked younger brother in 3 brother
# ----------------------------------------

# ali_age = int(input("Enter a ali age "))
# daim_age = int(input("Enter a daim age "))
# kamran_age = int (input("Enter a kamran age "))

# if ali_age<daim_age:
#     if ali_age<kamran_age:
#         print("Ali is a younger brother ")

# elif daim_age < kamran_age:
#     if daim_age<ali_age:
#         print("daim is a younger brother")
# else:
#     print("kamran is a younger brother")


# ______________________________________________________________________________________
# ______________________________________________________________________________________
# Q6 --> chacked eldest brother in 3 brother
# ---------------------------------------------

# ali_age = int(input("Enter a ali age "))
# daim_age = int(input("Enter a daim age "))
# kamran_age = int (input("Enter a kamran age "))

# if ali_age>daim_age and ali_age>kamran_age:
#     print("Ali is a eldest brother ")
# elif daim_age>ali_age and daim_age>kamran_age:
#     print("Daim is a eldest Brother ")
# else:print("Kamran is a eldest brother ")


# ______________________________________________________________________________________
# ______________________________________________________________________________________
# Q7 --> cheacked character is vowel or consanent
# -------------------------------------------------

# char = input("Enter a Alphabate : ")
# if char =='a' or char=='e' or char=='i' or char=='o' or char=='u' or char=='A' or char=='E' or char=='I' or char=='O' or char=='U':
#     print("This is a vowel ")
# else:
#     print("This is a consanent ")

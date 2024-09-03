
# enter your date biirth
birth_date=int(input("enter your birth date:"))
birth_month=int(input("Enter your birth month : "))
birth_year=int(input("inter your birth year :"))
print(f"your Birth date Is {birth_date}/{birth_month}/{birth_year}")
# enter a current year
current_date=int(input("Enter a current date: "))
current_month=int(input("Enter a current month: "))
current_year=int(input("Enter a current year: "))
print(f"Curret date is  {current_date}/{current_month}/{current_year}")
age_year=current_year-birth_year

age_month=age_year*12-10
age_date=age_year*365
print(f"Your Age is {age_year} years {age_month} Months {age_date} Days")  
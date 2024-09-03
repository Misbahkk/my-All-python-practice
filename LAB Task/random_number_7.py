# import random 
# first_num = int(input("Enter the start number : "))
# last_num = int(input("enter the last Num : "))
# prize= input("Enter the Prize name : ")
# lucky_numbers=int(input("Enter the number that win the prize : "))
# # create the empy lis
# numbers=[]
# # start loop for give the random number
# for i in range(lucky_numbers):
#     random_number=random.randint(first_num,last_num)
#     numbers.append(random_number)
# # this Line remove the dublicate number because set is uniquely indentifier
# unique_lucky_numbers = set(numbers)
# # Know conver the set into list
# new_list = list(unique_lucky_numbers)
# # Finaly print the Luky Numbers   
# print(f"The Lucky {lucky_numbers} Numbers those win the prize is : ")
# for number in numbers:
#     print(number)
    
# _________________________________________________________________________________
# _________________________________________________________________________________




import random 

first_num = int(input("Enter the start number : "))
last_num = int(input("enter the last Num : "))
prize= input("Enter the Prize name : ")
lucky_numbers=int(input("Enter the number that win the prize : "))

# genrate the random number and not repitive number..

numbers = set(random.sample(range(first_num , last_num + 1), lucky_numbers))

print(f"The Lucky {lucky_numbers} Numbers those win the prize is : ")
for number in numbers:
    print(number)



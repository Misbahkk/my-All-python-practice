# num =input("Enter a number ")
# print("enter a tabel : ")
# try:
#     for i in range(1,11):
#         print(f"{int(num)} X {i} = {int(num)*i}")
# except:
#     print("Invalid Num ! ")
# print("Important code")

# try:
#     num=int(input("Enter a integer : "))
#     a= [6,3]
#     print(a[num])
# except ValueError as e:
#     print(e)
# except IndexError as e:
#     print(e)

# ------------------------------------------------------------------
# Finally keyword--> always executed also in funtion
# ------------------------------------------------------------------
# def tabel():
#     num =input("Enter a number ")
#     print("enter a tabel : ")
#     try:
#         for i in range(1,11):
#             print(f"{int(num)} X {i} = {int(num)*i}")
#     except:
#         print("Invalid Num ! ")
#     # finally:  #--> When we not use finally then this print line not executed
#     print("Important code")
# x = tabel()


# ------------------------------------------------------------------
# Raise custom error
# ------------------------------------------------------------------
# a= int(input("Enter a num 5 to 9 and quite : "))
# if (a <5 or a>9 or a!="quite"):
#     raise ValueError("Value should be 5 to 9 ")
# else:
#     print("You are write")
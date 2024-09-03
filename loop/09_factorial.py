# num = int(input("Enter num "))
# factorial = 1
# for i in range(1,num+1):
#     factorial=factorial*i
# print(f"factorial is {factorial}")
# -----------------------------------------------------------------------------------------------
# Factorial by resursion
# -----------------------------------------------------------------------------------------------
# def Factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n* Factorial(n-1)
# print(Factorial(5))
# -----------------------------------------------------------------------------------------------
# Fibbonic series
# -----------------------------------------------------------------------------------------------
# def fibbonic(n):
#     if n<2:
#         return 1
#     else:
#         return fibbonic(n-1)+ fibbonic(n-2)
# for i in range(0,9):
#     print(fibbonic(i))
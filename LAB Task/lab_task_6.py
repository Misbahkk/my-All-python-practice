# Task No.1  --> This ia a factorial task
# def fact(num):
#     factorial=1
#     for i in range(1,num+1):
#         factorial*=i
#     return factorial
# a=int(input("enter a number for calculate the factorial : "))
# x=fact(a)
# print(f"{x}! is a factorial of {a}")

# ------------------------------------------------------------------------------
# TASK NO.2  --->Fibbonic Series
# def fib(end):
#     a=0
#     print(a)
#     b=1
#     print(b)
#     c=a+b
#     print(c)
#     for i in range(0,end+1):
#         a=b
#         b=c
#         c=a+b
#         print(c,end=",")
# print(fib(7))


# ----------------------------------------------------------------------------
# TASK NO.3
# def isPrime(num):
#     for i in range(2,num):
#         if num%i==0:
#             break
#         else:
#             print(num)
# isPrime(20)


x = input("Enter String: ")
y = len(x)
i = 0
new_string = ""

while i != y:
    new_char = chr(ord(x[i]) + 1)
    new_string += new_char
    i = i + 1

print(new_string)

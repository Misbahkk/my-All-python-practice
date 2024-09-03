#Q1 --> PRINT A TABLE 
# num = int(input("Enter a table "))
# for i in range(1,11):
#     print(num," x ",i,' = ',(i*num))
#     i=i+1
# _______________________________________________________________________________
# _______________________________________________________________________________

# Q2--> print a cube series
# i=1
# while i<10:
    
#     print(i*i*i,",")
#     i=i+1

# _______________________________________________________________________________
# _______________________________________________________________________________

# Q3--> print starik 
# for i in range(1 , 2000):
#     print('*',end="")

# _______________________________________________________________________________
# _______________________________________________________________________________

# Q4 --> count spaces character words
# sentence = input("Enter a Sentence : ")

# character =0
# words=1
# for i in sentence:
#     if i!=' ':
#         character=character+1
#     elif i==' ':
#          words = words+1
# print('total words ', words)
# print('total character ',character)
# space=words-1
# print('total space ',space)

# _______________________________________________________________________________
# _______________________________________________________________________________
# Q5 --> calculate the sum and average 
# ------------------------------------

# sum = 0
# for i in range(1,11):
#     num = int(input('Enter a num '))
#     sum = sum + num
# average = sum/10
# print("sum of 10 num is : ",sum)
# print(f"Average of 10 sum {sum} num is {average}")    



# _______________________________________________________________________________
# _______________________________________________________________________________
# Q6 -->genrate the fibbonic series
# ----------------------------------

# a=0
# print(a)
# b=1
# print(b)
# c=a+b
# print(c)
# for i in range(1,7):
#     a=b #1
#     b=c #1
#     c=a+b #2
#     print(c)



# _______________________________________________________________________________
# _______________________________________________________________________________
# Q7--> enter a 2 num and 1 is base 2nd s power

# base = int(input('Enter a base : '))
# mul=1
# power = int(input("Enter a power : "))
# for i in range(1,power+1):
#     mul*=base
# print(mul)


# _______________________________________________________________________________
# _______________________________________________________________________________
# Q8--> calculate the factorial

# num = int(input("Enter a number : "))
# factorial = 1
# for i in range (1,num+1):
#     factorial *=i
# print(f"factorial of {num}! is {factorial}")


# _______________________________________________________________________________
# _______________________________________________________________________________
# Q9--> PRINT A PRIME NUMBER 

# for num in range(1,1000):
#     isprime=True
#     for i in range(2,num):
#         if(num%i)==0:
#             isprime=False
#     if isprime:
#         print(num)


# _______________________________________________________________________________
# _______________________________________________________________________________
# Q10--> print a star in different method
# ------------------------------
# STAR PRINT IN DAIMOND FORM
# -----------------------------
# n=6
# for i in range(n):
#     for j in range(i,n):
#         print(' ',end=' ')
#     for j in range(i-1):
#         print('*',end=' ')
#     for j in range(i):
#         print('*',end=' ')
#     print()
# for i in range(n):
#     for j in range(i):
#         print(' ',end=' ')
#     for j in range(i,n-1):
#         print('*',end=' ')
#     for j in range(i,n):
#         print('*',end=' ')
#     print()           


# --------------------------------------------
        
        
# n=6
# p=1
# for i in range(n):
    
#     for j in range(i,n):
#         print(' ',end=' ')
#     for j in range(i-1):
#         print(p,end='   ')
#         p+=1
    
#     print()    



# n=6
# for i in range(n):
#     p=65
#     for j in range(i,n):
#         print(chr(p),end=' ')
#         p+=1
#     for j in range(i):
#         print("-",end='')
#     b=70
#     for j in range(i,n):
#         print(chr(b),end=' ')
#         b-=1
    
#     print()    


n=7
k=1
for i in range(n):
    p= 65
    for j in range(i,n):
        print(chr(p),end=' ')
        p+=1
    for j in range(i):
        print(" ",end="")
    b=71-k
    for j in range(i+1):
        print(" ",end="")
        # l=1
    for j in range(i,n-1):
        print(chr(b),end=" ")
        b-=1
        # l-=1
    print()
    k=k+1
    

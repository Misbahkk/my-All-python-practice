# Question - 1   search the index the number in array 
# ----------------------------------------------------------------------------------------
# arr=[]
# for i in range(1,11):
#     x = int(input("Enter the 10 Numbers: "))

#     arr.append(x)
# print(arr)
# # arr=[21,23,32,43,54,65,76,87,98,90,11]

# print(arr)
# serch = int(input("enter a serch the number :"))
# print(serch," index is --> ",arr.index(serch))


# ----------------------------------------------------------------------------------------
# QUESTION - 2 --> made the array linst and count the positive , negative , od , even number
# ----------------------------------------------------------------------------------------
# arr=[21,-23,-32,43,54,-65,76,-87,98,90,11]
# print('Number is Negative')
# for i in arr:
#     if i < 0:
#         print(i,end=",")

# print('Number is Positive')
# for i in arr:
#     if i>0:
#         print(i ,end=",")

# print("Number is Even")
# # Number is Even
# for i in arr:
#     if i%2==0:
#         print(i,end=",")

# ----------------------------------------------------------------------------------------
# QUESTION - 3 --> 1 arry is copy to another arry and reverse th array
# ----------------------------------------------------------------------------------------
# arr = [21,22,33,44,55,66,77,88]
# print(arr)
# arr1 = arr.copy()
# arr1.reverse()
# print(arr1)
#----------------------------------------------------------------------------------------
# QUESTION - 4 -->reverse the sitring
#----------------------------------------------------------------------------------------
# str =  input("Enter the String : ")
# words= str.split()
# x=len(str)
# print(x)

# rev_string = [word[::-1] for word in words]
# rev = ' '.join(rev_string)
# print(rev)


#----------------------------------------------------------------------------------------
# QUESTION - 5  --> take input strig and sun ascii code
#----------------------------------------------------------------------------------------

# str = input("Enter a String : ")
# code = 0
# # arr = str.split()
# for char in str:
#    code+=ord(char)

# print(code)

#----------------------------------------------------------------------------------------
# QUESTION - 6 
#----------------------------------------------------------------------------------------
# str = input("enter a Singel word : ")
# arr = str.split()
# for i in arr:
#     for j in range(i):
#         print("*" , end=" ")
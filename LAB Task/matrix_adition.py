# This is code of first matrices input
arr1=[]
matr_1=[]
for i in range(3):
     for i in range(3):
          x = int(input("Enter the 3 Numbers: "))

          arr1.append(x)
     if len(arr1)==3:
          arr2=arr1
          arr1=[]
     matr_1.append(arr2)
     print(matr_1)
# This ia a code of 2nd matrices input
arr3=[]
matr_2=[]
for i in range(3):
     for i in range(3):
          x = int(input("Enter the 3 Numbers: "))

          arr3.append(x)
     if len(arr3)==3:
          arr4=arr3
          arr3=[]
     matr_2.append(arr4)
     print(matr_2)
# adding the 2 matricess
result=[[0,0,0],[0,0,0],[0,0,0]]
x = len(matr_1)
for i in range(x):
    for j in range(len(matr_1[0])):
        result[i][j] = matr_1[i][j] + matr_2[i][j]
print(result)

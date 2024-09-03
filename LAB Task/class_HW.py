# calculate Average HW grade
print("This Program computes Yor avrage Home Work Grades")

assigment = int(input("How Many Assigment Wer there? "))
obtain =0
total =0
for i in range(1 , assigment+1):
    print("Assigment No: ",i)
    point = int(input("points Earned? "))
    
    point_possible = int(input("point possible? "))
    while point>point_possible:
       print("Enter valid point possible number")
       point_possible = int(input("point possible? "))
    obtain = obtain + point 
    total = total + point_possible
average = obtain/total*100
print("Total Assigment Markx is : ",total)
print("You Obtain markx in assigment : ",obtain)
print("Your Avrage Marks is :" , average ,"%")


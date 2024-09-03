print("Hey!! This Is MY File Handling HW There are 3 opetion \n 1.write ,2.read , 3.append")
fileName="Function Name"
x="read"
y="write"
z="append"
def readFile():
        file_name=input("Your file name : ")  
        f=open(file_name,"r")
        # x=True
        roll_numbers=f.readlines()
        # while(x):
          
        #   word=input("Entr a roll number ")
        #   if word == "exit":
        #     break
        #   match word:     
        #     case 1:
        #         for lines in line:
        #           if lines.find(word)!= -1:
        #             print("word is present ")
        #     case 2:
        #           print("Enter Roll number")  

        roll_number = input("Enter a roll number to search for: ")
        roll_number_found=False
        for roll in roll_numbers:
        
          if roll.find(roll_number) != -1:
            roll_number_found = True
            break
        if roll_number_found:
          print(roll_number,"Roll number found in the file.")
          print("Line",roll)
        else:
          print("Roll number not found in the file. Please enter a valid roll number.")

        f.close()
def writeFile():
    f=open("data.txt","w")
    data=input("Enter Your file data that you save:\n ")     
    print(data,file=f)
    f.close()
def appendFile():
    f=open("data.txt","a")
    data=input("Enter Your file data:\n ")
    print(data,file=f)
    f.close()
while fileName != "exit": 
    fileName=input("write a function name That you want ... ")   
    match fileName:
        case _ if fileName==x:
           readFile()
        case _ if fileName == y:
           writeFile()
        case _ if fileName == z:
           appendFile()
print("You exit the program")
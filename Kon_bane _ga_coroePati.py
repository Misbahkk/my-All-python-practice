# Write a program to kon bane ga corer pati
Questions=["What is your country name ","Pakistan kb azad hova ", "who is the first founder of pakistan "]
amount=0
Answers= ["Pakistan","14-Augest","Quaid"]
for i in range(0,3):
   Answer = input(Questions[i])
   if Answer==Answers[i]:
      print("correct Answer!! You Gote 50$")
      amount+=50
   else:
      print("wrong answer!! you lose 50$")
      amount-=50

   
print("Total Amount: ",amount)
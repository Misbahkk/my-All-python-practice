x = int(input("Enter a num : "))
match x:
    case _ if x==0:
        print(x,"is 0")
    case _ if x ==10:
          print(x,"is equal to 10")
    case _ if x ==20:
          print(x,"is equal to 20")
    case _ if x ==30:
          print(x,"is equal to 30")
    case _ if x ==40:
          print(x,"is equal to 40")
    case _ :
          print(x,"is equal to all")

num = int(input("Enter the number: "))

prime = True
for i in range(2,num):
    if(num%i==0):
        prime=False
        break
if prime:
    print("This num is prime")
else:
    print("This num is mnot prime")
    
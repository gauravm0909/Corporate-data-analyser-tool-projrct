#qno.1
num=int(input("Enter the number:"))
if(num%2==0):
    print("even")
else:
    print("odd")
#qno.2
num1=int(input("Enter the 1st number:"))
num2=int(input("Enter the 2nd number:"))
num3=int(input("Enter the 3rd number:"))
if(num1>num2 and num1>num3):
    print("largest no.is:",num1)
elif(num2>num3):
    print("largest no.is:",num2)
else:
    print("largest no.is:",num3)
    #qno.3
num4=int(input("Enter the number:"))
if(num4%7==0):
    print("It is a multiple of 7.")
else:
    print("Not a multiple of 7")
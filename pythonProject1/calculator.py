print("Enter two value:")
value1=input("value 1 is:")
value2=input("value 2 is:")
opt=int(input("Enter 1 for '+' : Enter 2 for '-' : Enter 3 for '*': Enter 4 for '/':"))
if opt==1:
    if int(value1)==56 and int(value2)==9:
        print("Your result =77")
    else:
        a=int(value1)+int(value2)
        print("Your result =",a)
elif opt==2:
    b=int(value1)-int(value2)
    print("Your result=",b)
elif opt==3:
    if int(value1)==45 and int(value2)==3:
        print("Your result=555")
    else:
        c=int(value1)*int(value2)
        print("Your result=",c)
elif opt==4:
    if int(value1)==56 and int(value2)==6:
        print("Your result=4")
    else:
        d=int(value1)/int(value2)
        print("Yuor result=",d)
else:
    print("Your option is wrong:")

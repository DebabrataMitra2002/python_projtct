# a=[1,2,34,24,154,34,46,77]
# for x in a:
# #     print(x)
# a=7
# # for x in range(1,11):
# #     print(a ,"*",x,"=",a*x)
# def fun1():
#     print(" my name is debabrata")

# print(fun1())

# number=int(input("Enter the number for cheeking prime:"))
# prime =True
# for x in range(2,number):
#     if(number%x==0 and number!=2):
#         prime=False
#         break
# if prime:
#     print("Number"+str(number)+"is prime:")
# else:
#     print("Number"+str(number)+"is not prime:")

"""
num=int(input("Input number of term :"))
x=1
sum=0
while(x<=num):
 sum=sum+x
 x=x+1
print(f"sum = {sum}")
"""
n=int(input("Enter the no of row and col:"))

for i in range(1,n+1):
    for j in range(1,n+1):
        if(((i==1)or(i==n))or(((j==1)or(j==n)))):
            print("*",end="")

        else:
            print(" ",end="")
    print()            





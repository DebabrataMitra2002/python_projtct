# a=("2")
# print(type(a))
# a=["1","2","3","4","5","5"]
# b=set(a)
# b=list(b)
# print(b)
# disc ={
#     1: "sunday",
#     2: "monday",
#     3: "tuesdeay",
#     4: "wednesday"
# }
# for i in disc:
#    print(disc[i])
# else:
#    print("Enter the right value:")
class Addition:
   #  first_num=0
   #  sec_num=0
   #  a=0
    def __init__(self,first,second):
        self.first_num=first
        self.sec_num=second

    def display(self):
        self.a=self.first_num+self.sec_num
        print("Sum is equal to :",self.a)

p1=Addition(23,34)
p1.display()
# class Addition:
# 	first = 0
# 	second = 0
# 	answer = 0

# 	# parameterized constructor
# 	def __init__(self, f, s):
# 		self.first = f
# 		self.second = s

# 	def display(self):
# 		print("First number = " + str(self.first))
# 		print("Second number = " + str(self.second))
# 		print("Addition of two numbers = " + str(self.answer))

# 	def calculate(self):
# 		self.answer = self.first + self.second


# # creating object of the class
# # this will invoke parameterized constructor
# obj1 =Addition(1000, 2000)

# # creating second object of same class
# obj2 = Addition(10, 20)

# # perform Addition on obj1
# obj1.calculate()

# # perform Addition on obj2
# obj2.calculate()

# # display result of obj1
# obj1.display()

# # display result of obj2
# obj2.display()

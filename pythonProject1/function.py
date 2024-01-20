'''        Function Decorator

A decorator is a function that takes a function as its only parameter and returns a function. This is helpful to “wrap” functionality with the same code over and over again. For example, above code can be re-written as following.
We use @func_name to specify a decorator to be applied on another function.
'''


# def Wellcome():

#     return print("Wellcome to python :")


# Wellcome()


def greet(fun):
    def wello():
        return "wellcome to my home "
    return wello() + fun()

# def name(a):
#  return a


# print (greet(name("bidisha")))
# @greet
def name(a):
    return a 
  
print (name("Dola") )

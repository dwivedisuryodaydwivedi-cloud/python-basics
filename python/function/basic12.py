# calculator using function
def add():
    x = int(input("enter your number x :"))
    y = int(input("enter your number y :"))
    z = x+y
    print(z)
    
def multiply():
    x = int(input("enter your number x :"))
    y = int(input("enter your number y :"))
    print(x*y)
    
def subract():
    x = int(input("enter your number x :"))
    y = int(input("enter your number y :"))
    print(x-y)
    
def divide():
    x = int(input("enter your number x :"))
    y = int(input("enter your number y :"))
    print(x/y)
    
def modulo():
    x = int(input("enter your number x :"))
    y = int(input("enter your number y :"))
    print(x**y)

def reminder():
    x = int(input("enter your number x :"))
    y = int(input("enter your number y :"))
    print(x%y)

add()
multiply()
subract()
divide()
modulo()
reminder()

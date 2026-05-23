# if-else conditional statements
a = 45
b =54
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")

# check given number is above 20 or not
num = int(input("enter your number is : "))
if num > 20:
    print("number is above 20") 
else:
    print("number is below 20")

    # checking the given number is even or odd 
    num = int(input("enter your number :"))
    res = num % 2
    if res == 0:
        print("number is even ")
    else:
        print("given number is odd")

    # checking the value in between variable which is greater
    x = int(input("enter your number x is : "))
    y = int(input("enter your number is y :"))
    if x > y:
        print("x is greater :")
    else:
        print("y is greater")

    # if else using nesting conditions 
    # nuber is graeter or not
    num = int(input("enter your number is : "))
if num >= 20:
    if num > 20:
        print("number is above 20")
    else:
        print("number is equal")

else:
    print("number is below 20")

    # checking the value in between variable which is greater

    x = int(input("enter your number x is : "))
    y = int(input("enter your number is y :"))
    if x >= y:
        if x > y:
            print("x is greater :")
        else:
            print("number is equal")
    else:
        print("y is greater")
     


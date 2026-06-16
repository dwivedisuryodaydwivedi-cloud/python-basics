# fuction type 3rd type with reaturn without argument 
# printing the factorial of a number by using function with return without argument
def fact():
    num = int(input("enter your number :"))
    f = 1
    if num>0:
        for i in range(1,num+1):
            f = f*i
        return f
    else:
        f = 0
        return f
    
fact()
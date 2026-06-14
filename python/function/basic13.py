# function type one problem without return without argument
# using function findind the fectorial of a number 

 
def fact():
    num = int(input("enter your number:"))
    fact = 1
    if num >= 0:
        for i in range(1,num+1):
            fact = fact*i
            print(fact)
    else:
        fact = 0
        print(fact)
fact()

# # Write a program to check the given number is prime number or not by using fuction 1st type 
# def prime():
#     num = int(input("enter your number is :"))
#     i = 2
#     while i<num:
#         if num % i== 0:
#             print("is not prime number")
#             break
#         i = i+1
#     if i == num:
#         print("prime number")
# prime()


# wap to print the power of x to the power by using loop without using exponet function
# def power():
#     x = int(input("enter your number x"))
#     y = int(input("enter your number y"))
# #     power = x ** y
# #     print("power is power",power)
# # power() its simple methode to print the power of number by using exponential operator 
#     result = 1
#     for i in range(1,y+1):# here y says how much time our loop is runnig 
#         result = result * x # result printing the original value
#         print("result is result ", result)
# power()

# # checking the input number is even or odd 
# def check():
#     num = int(input("enter your number is :"))
#     if num%2==0:
#         print("even number")
#     else:
#         print("not prime number")
# check()

# # printing the series of odd number upto n 
# def odd():
#     num = int(input("enter your number :"))
#     for i in range(1,num,2):
#         print("odd number of n is ",i)
# odd()

# def sum():
#     num = int(input("enter your number :" ))
#     sum = 0
#     for i in range(1,num+1,1):
#         sum = sum + 1
#         print(sum)
# sum()
# # printing table using function 
# def table():
#     num = int(input("enter your number :"))
#     for i in range(1,11,1):
#         table = num * i
#         print("the table of given number is", table)
# table()

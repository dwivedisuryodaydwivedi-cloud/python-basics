# loops for loop and while loop 
# problem 1 
i = 1 
while i <= 10:
    print("Hello World  ") 
    i = i + 1

# write a program to print the number from one to ten 
i = 1 
while i <= 10:
    print(i)
    i = i + 1 

# write a program to print number which is even nummber 
num = int(input("enter your number is "))
i = 1
while  i <= num :
    if i %2 == 0:
        print(i)
    i = i + 1

# print the series of odd number upto n number 
num = int(input("enter your number :"))
i = 1 
while i <= num:
        print(i)
        i = i + 2

# the sum first 10 numbers 
n = int(input("enter your number is :"))
i = 1
sum = 0
while i <= n:
    sum = sum + i
    i = i + 1
    print("the sum of n natural numbers ", sum)

# wap to print number of any table by taking input from user 
n = int(input("enter your number n :"))
i = 1 
while i <= 10:
    print(n * i)
    i = i + 1

# finding the fectorial of given input number 
n = int(input("enter your number is :"))
i = 1
fact = 1
while i <= n:
    fact = fact * i
    print("factorial of n numbers is", fact)
    i = i + 1
    
        

        
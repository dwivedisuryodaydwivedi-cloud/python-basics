# dATE : 25-05-26
#  Make a program to take basic salary, allowance and taxes of a employee. 
# And calculate the Total salary  (salary+allowance-tax) and display it. 
salery = int(input("enter salery of an employee :"))
alloWance = int(input("enter allowance of an employee :"))
tax = int(input("enter the tax of an employee :"))
total_salery = salery + alloWance - tax 
print("total salery of an employee is :",total_salery)

# PROBLEM 2 
# # WAP a program to check the given year is leap year or not 
year = int(input("enter year is :"))
if year %4==0:
    print("year is a leap year ")
else:
    print("year is not a leap year ")
    
# problem 3
# find the greatest variable values between thtee variables 
num1 = int(input("enter your num1 is :"))
num2 = int(input("enter your num2 is :"))
num3 = int(input("enter your num3 is :"))

if num1 > num2 and num1 > num3:
    print("num1 is greater")
elif num2 > num3 and num2 > num1:
    print("num2 is greater")
else:
    print("num3 is greater ")

# CHECKING THE NUMBER ENTERED BY THE USER IS EVEN OR ODD
num = int(input("enter your number :"))
if num % 2 == 0:
    print("number is even ")
else:
    print("number is odd ")
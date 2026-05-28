# operators # arithmetic operators
x = int(input("enter value of x:"))
y = int(input("enter the value of y:"))
z = x ** y 
print("exponential is :",z)
z = x // y
print("floor division is :",z)

x = int(input("enter the value of x "))
y = int(input("enter the value of y "))

print("x + y =",x+y)
print("x - y =",x-y)
print("x * y =",x*y)
print("x / y =",x/y)


# relational operators
x = int(input("enter the value of x :"))
y = int(input("enter the value of y :"))

print("x > y =",x>y)
print("x < y =",x<y)
print("x == y =",x==y)
print("x != y =",x!=y)
print("x >= y =",x>=y)
print("x <= y =",x<=y)

# logical operators
x = int(input("enter the value of x :"))
y = int(input("enter the value of y :"))
z = int(input("enter the value of z :"))
res = (x == y) and (x == z) and (y == z)
print("logical AND :", res)
res = not(x == y) or (x==z) or (y==z)
print("logical OR :", res)
res = (x == y) and (x == z) and (y==z)
print("logical not :", res)
''' ex : x = 11 , y = 22 , z = 22 
res = (x == y)and (x == z) and (y == z)
    = (11 == 22)and (11 == 22) and (22 == 22)
     false and false and true 
      false or true 
       true 
       res = (x == y)and (x == z) and (y == z)
    = (11 == 22) or (11 == 22) or (22 == 22)
     false or  false or true 
      false or true 
       true
       res = not(x == y)and (x == z) and (y == z)
    = not(11 == 22)and (11 == 22) and (22 == 22)
     not(false and false and true)
      not(false or true)
       true 
         '''

x = int(input("enter the value of x :"))
y = int(input("enter the value of y :"))
z = int(input("enter the value of z :"))

res = (x == y )and (x ==z)or (y == z)
print("logical AND-OR :",res) 

res = (x == y) or (x == z) and (y == z)
print("logical OR-AND :", res)

# some basic questions on operators 
#Check whether a number is between 10 and 50 using logical operators.
num = int(input("enter your number is : "))
num1 = (num > 10) and ( num < 50)
print("the number is in between 10 and 50:",num1)

# Write a program to check if a person is eligible to vote:
age = int(input("enter your age : "))
eligible = (age == 18) or (age > 18) 
print("person is eligible to vote :", eligible)

# check wheter the number is divisible by both 3 and 5
num = int(input("enter your number :"))
divisible = (num %3== 0) and (num %5== 0)
print("number is divisible by both 3 and 5", divisible)

# Check whether a character is a vowel using or.
char = input("enter your character :")
vowel = (char == 'a') or (char == 'e') or (char == 'i') or (char == 'o') or (char == 'u') or (char == 'A') or (char == 'E') or (char == 'I') or (char == 'O') or (char == 'U')
print("character is vowel :", vowel)

# Check whether a student passed:

# marks greater than 33
# attendance greater than 75%

marks = int(input("enter your marks :"))
attendance = int(input("enter your attendance:"))
checking = (marks > 33 ) and (attendance > 75 )
print("student is pass :",checking)
 
         

         


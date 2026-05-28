# date 20/05/26
# input in python 
# this function is used for gert data from user via consol window this function returns string type of value 
# data = input()
# data = input("enter any data :")
# print("data value is : ", data)
# print(type(data)) # type printing 
# print("bye .....")

# x = input("enter the value of x :")
# print("value of x is :",x)
# y= input("enter the value of y :")
# print("value of y is :",y)
# print(type(y))
# z = x+y 
# print("value of z is : ", z)
# print(type(z))

# # type casting in python 
# x = "10"
# print("value of x :", x)
# print(type(x))
# a = int(x)
# print("value of a is ", a)
# print(type(a))

# # x = 10
# x = 20.5
# print("value of x is :", x)
# print(type(x))
# print()
# #a float(x)
# a = int(x)
# print(type(a))

# x = input("enter your value of x :")
# print("value of x is :",x)
# print(type(x))
# y = input("enter value of : ")
# print("value of y is :",y)
# print(type(y))
# z = int(x)+int(y)
# print("value of z is :",z)
# print(type(z)) 

# # assignment two input in python with data type 
# x = input("enter value of x :")
# y = input("enter value of y :")
# print(x)
# print(y)
# print() # line change :/n 
# print("value of x is :", x)
# print("value of y is :", y)
# print()
# print(x," : ",y)
# print("value of x : ", x , " : value of y : ",y)
# print()

 # note : , is used for conacat 

# assinement one date 19/05/2026
# Q1 subtraction, multiplication, division, modulus, of two variable 
x = int(input("enter value of x :"))
y = int(input("enter value of y :"))
print(x - y)
print(x / y)
print(x * y)
print(x % y)


# Q2 CALCULATE SIMPLE INTREST 
# simpe intrest formula is SI = (p * r * t)/ 100
p  = int(input("enter value of principal amount:")) # principal amount 
r = int(input("enter value of rate of intrest :")) # rate of intresrt 
t = int(input("enter value of time in year :")) # time in years 
SI = (p * r * t) / 100
print("simple intrest is : " , SI)


# Q3 area of rectangle 
# # area of rectangle is A = L * W  
length = int(input("enter length of an rectangle is :")) 
width = int(input("enter width of an recgangle is :")) 
area = length * width 
print("area of rectangle is : ", area)

# area of triangle is 1 / 2 base * height 
base = float(input("enter base of an triangle is :"))
height = float(input("enter height of an triangle is :"))
area =(1/2 * base * height)
print("area of triangle is :", area)

# area of circle is pia * r * r (r = radius)
radius = float(input("enter radius of an circle is :"))
area = (3.14 * radius  * radius) # pia = 3.14 
print("area of circle is :", area)

# area of square is area = s * s 
side = int(input("enter side of an square is :")) 
area = side * side 
print("area of square is :", area )
print(type(area))

# Q4 swapping of two numbers by using third variable 
x = input("enter value of x :")
y = input("enter value of y :")
z = input("enter value of z :")
# assigning value 
z = x 
x = y 
y = z
print("value of x :", x , "value of y :" , y)

# Q5 swapping of two numbers without using third variable
x = input("enter value of x :")
y = input("enter value of y :")

# assigning value 
x , y = y , x
print("value of x :", x , "value of y :" , y)



 











# problem 1
# Take values of length and breadth of a rectangle from user and check if it is square or not.

length = int(input("enter length of an rectangle :"))
breadth = int(input("enter breadth of an rectangle :"))
if length == breadth:
    print("is a square ")
else:
    print("is not a square ")

# problem 2

""" Python program to print the following string in a specific format (see the output).  String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in  the sky. Twinkle, twinkle, little star, How I wonder what you are" Output : 
Twinkle, twinkle, little star, 
 How I wonder what you are!  
 Up above the world so high,
 Like a diamond in  the sky.
Twinkle, twinkle, little star,  
 How I wonder what you are """
poem = ("Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in  the sky. Twinkle, twinkle, little star, How I wonder what you are ")
 
print("Twinkle, twinkle, little star,\n How I wonder what you are!  \n Up above the world so high,\n Like a diamond in  the sky.\n Twinkle, twinkle, little star,\n How I wonder what you are ")
 
""" problem 3
 Write a Python program which accepts the radius of a circle from the user and compute the area.
Output :
r = 1.1"""

Area = 3.8013271108436504 
radius = float(input("enter your radius of a circle:"))
area = 3.14 * radius * radius
print("area of circle is :", area)


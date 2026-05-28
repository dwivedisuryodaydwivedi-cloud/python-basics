# problem one 
# Write a Python program which accepts the user's first and last name and print them in reverse order with  a space between them. 
first_name = input("enter your first name :")
last_name = input("enter your last name :") 

# Write a Python program which accepts the user's first and last name and print them in reverse order with  a space between them. 
name = input("enter your name :")
surname = input("enter your surname :")
print("user name and surname",name + surname)
print("user surname and name in reverse order: ", surname + " " + name)

# problem 2
# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount.  
# 12. A school has following rules for grading system: 
# a. Below 25 - F 
# b. 25 to 45 - E 
# c. 45 to 50 - D 
# d. 50 to 60 - C 
# e. 60 to 80 - B 
# f. Above 80 - A 
# Ask user to enter marks and print the corresponding grade. 

marks = int(input("enter your marks :"))
if marks > 80 and marks <= 100:
    print("the employee has scored 'A' grade ")
elif marks > 60 and marks <=80:
        print("employee scored 'B' grade : ")
elif marks > 50 and marks <=60:
        print("employee has scored 'C' grade :")
elif marks > 45 and marks <= 50:
        print("employee has scored 'D' grade :")
elif marks > 25 and marks <= 45:
        print("employee has scored 'E' grade : ")
else:
    print("employee fails :")


# problem 3 
# . A student will not be allowed to sit in exam if his/her attendance is less than 75%. Take following input from user 
# Number of classes held 
# Number of classes attended. 
# And print 
# percentage of class attended 
# Is student is allowed to sit in exam or not 

classes_held = int(input("enter number of classes held :"))
classes_attend = int(input("enter number of classes attend :"))
# percentage = number of outcomes / total number of outcomes 
percentage = int((classes_attend / classes_held) * 100)
if percentage > 75:
    print("studnet are eligible to sit in exam ", percentage)
else:
    print("student is not eligibel to sit in exam ", percentage)

# problem 4 
# 17. Make a program to take 5 subject marks and calculate the total marks and percentage of a student.

maths = int(input("enter your maths marks :"))
physics = int(input("enter your maths physics :"))
chemistry = int(input("enter your chemistry marks :"))
hindi = int(input("enter your hindi marks :"))
GK = int(input("enter your GK marks :"))

sum = maths + physics + chemistry + hindi + GK
print(sum)
percentage = sum / 500 * 100
print("percentage of student is ", percentage)

# write a program to check given character is vowel or consonant
character = input("enter your character :")
if character in ('a', 'e', 'i', 'o', 'u'):
    print("character is vowel :")
else:
    print("character is consonant :")

        

        
# check given num into reverse order without using loop fpr three digit number
num = int(input("enter your number :"))
print("actual number is :", num)
rem1 = num % 10 
rem2 = (num//10)%10
rem3 = num//100
rev = rem1*100 + rem2*10+ rem3 
print("reverse number is :",rev)

# check given number is palindrome or not only for three digit number
num = int(input("enter your number is :"))
rem1 = num % 10 
rem2 = (num//10)%10
rem3 = num//100

rev = rem1*100 + rem2*10+ rem3
if num == rev:
    print("the given number is palindrome ")
else:
    print("given number is not palindrome :")

# check the given number is armstrong or not 
num = int(input("enter your number is :"))
print("actual number is :", num)
rem1 = num % 10 
rem2 = (num//10)%10
rem3 = num//100

# rem = rem1*rem1*rem1 + rem2*rem2*rem2 + rem3*rem3*rem3
rev = rem1**3 + rem2**3 + rem3**3
if num == rev:
    print("given number is palindrome ")
else:
    print("given number is not palindrome ")

# print marksheet between 3 subjects 






# with return with argument
def fact(num):
    f = 1 
    if(num >= 0):
        for i in range(1,num+1):
            f = f * i
            print("value of f is :", f)
        else:
            f = 0
        return f
res = fact(-1)
print("value of res is :", res)
fact(-1)


# # check given number is even or odd 
# def check(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
# res = check(23)
# if res:
#     print("given number is even :")
# else:
#     print("given number is odd :")

# """
# check given number is prime or not 
# """


# def add():
#     x = 22 
#     y = 22 
#     z = x+y
#     return z

# res = add()
# print("value of res is :", res)

# def fact():

#     num = int(input("enter any nummber to find factorial :"))
#     f = 1
#     if(num >= 0):
#         for i in range(1,num+1):
#             f = f * i
#     else:
#         f = 0
#     return f

# res = fact()
# print("value of res is :", res)

# # check given number is even or odd 
# def check():
#     num = int(input("enter any number to check even or odd "))
#     if num % 2 == 0:
#         return True
#     else:
#         return False
# res = check()
# if res:
#     print("given number is even :")
# else:
#     print("given number is odd :")

# """
# find the x to the power y without pre-define function and operator"""

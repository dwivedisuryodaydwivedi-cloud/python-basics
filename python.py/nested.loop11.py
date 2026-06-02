# nested loop in python 
# wap to print the nubmer from 1 to 5 in row and 1 to 6 coulam 
for i in range(1 , 6 , 1):
    for j in range(1 ,7 , 1):
        print("1", end= " ")# this syntax used to print the statement in same line because we know after printing in code it by default print next line 
    print()
print("bye....")

# wap to print the right angle of an nummbe in an increasing order 
for i in range(1, 6 , 1):
    for j in range(1 , i +1  , 1):
        print(j , end= " ")
    print()
print("bye....")
    
# WAP to print square of number in increasing order 
for i in range(1 , 6 , 1):
    for j in range(1, 6 , 1):
        print(j , end= " ")
    print()
print("bye....")
    
    
# wap to print the square pattern  in reverse order of number
for i in range(5 , 0 , -1):
    for j in range(5 , 0 , -1):
        print(j ,end= " ")
    print()
print("bye....")

# wap to print the right angle pattern of an element in an reverse order 
for i in range(5 , 0 , -1):
    for j in range(5 , i - 1 , -1):
        print(j , end= " ")
    print()
print("bye....")


# wap for printing the pattern of an element and alphabate in a square form 
for i in range(1 ,6 ,1):
    for j in range(1, 6 , 1):
        print("*", end= " ")
    print()
    
# wap for printing the pattern of an element and alphabate in a right angle  form 
for i in range(1 ,6 ,1):
    for j in range(1, i + 1 , 1):
        print("*", end= " ")
    print()
    

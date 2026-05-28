p = int(input("Enter Physics Marks : "))
c = int(input("Enter Chemistry Marks : "))
m = int(input("Enter Maths Marks : "))


if (p > 0 and p < 100) and (c > 0 and c < 100) and (m > 0 and m < 100):
 if p < 33:
  if c < 33:
    if m < 33:
      print("Fail in All Subjects : ")
    else:
      print("Fail in Phy & Chem : ")  
  else:
    if m < 33:
      print("Fail in Phy & Maths : ")
    else :
      print("Suppli in Phy : ")
 else:
  if c < 33:
    if m < 33:
      print("Fail in Chem & Maths ")
    else :
      print("Suplli in Chem : ")  
  else:
    if m < 33:
      print("Suppli in Maths : ")
    else:
         total = p + c + m 
         per = total // 3
         if per >= 75:
           print("Pass in A+ Grade : ",per)
         elif per >= 60:
           print("Pass in A Grade : ",per)
         elif per >= 55:
           print("Pass in B Grade : ",per)                      
         elif per >= 45:
           print("Pass in C Grade : ",per)
         else:
            print("Pass in All Subjects : ",per) 
else:
 print("Invalid Marks : cannot Enter Above 100 or -ve Marks ")   
 
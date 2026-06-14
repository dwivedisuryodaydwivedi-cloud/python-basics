def login():
    username = input("enter your username :")
    password = input("enter your password :")
    if username == "admin" and password == "admin":
        print("admin login successfully....")
    elif username == "feculty" and password == "feculty":
        print("feculty login successfully....")
    elif username == "student" and password == "student":
        print("student login sucessfully...")
    else:
        print("invalid username and password")
    
login()

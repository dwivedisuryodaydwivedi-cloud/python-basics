print("before function invoked :")
def show():
    print("show function innvoked ")
def wish():
    print("wish invoked :")
    show()

show()
wish()
print("after function invoked :")
print("bye.....")
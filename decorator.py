def login_page(login):
    def wrapper(user,password):
        if user=='admin' and password=='1234':
            print("Login successfull")
            login_page()
        else:
            print("Login failed")
    return wrapper

@login_page
def login(user,password):
    print("welcom to application")

login('admin',2234)
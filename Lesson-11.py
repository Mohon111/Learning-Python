#constructor
class test_class:
    def __init__(self):
        print("I am a constructor")

    def function_1(self):
        print("I am a function")

    def function_2(self):
        print("I am another function")

Object_1 = test_class()
Object_1.function_2()

#Lesson-10
class User:
    name = ""
    email = ""
    password = ""
    login = False

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def Login(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        if(email == self.email and password == self.password):
            login = True
            print("Login Successful!")
        else:
            print("Login Failed!")

    def Logout(self):
        login = False
        print("Logged Out")

    def IsLoggedIn(self):
        if (self.Login):
            return True
        else:
            return False

    def Profile(self):
        if self.IsLoggedIn():
            print(self.name, "-", self.email)
        else:
            print("Not Logged In!")

User1 = User("Mohon Basu", "mahendrabashumohon@gmail.com", "12345")
# User1.name = "Mohon Basu"
# User1.email = "mahendrabashumohon@gmail.com"
# User1.password = "12345"
User1.Login()
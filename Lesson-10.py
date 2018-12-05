#OOP(class)
class User:
    name = ""
    email = ""
    password = ""
    login = False

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

User1 = User()
User1.name = "Mohon Basu"
User1.email = "mahendrabashumohon@gmail.com"
User1.password = "12345"
User1.Login()
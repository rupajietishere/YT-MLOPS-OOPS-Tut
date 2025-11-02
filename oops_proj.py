class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()



    def menu(self):
        user_input = input("""Welcome to Chatbook!! How would you like to proceed?
                            1. Press 1 to SignUp
                            2. Press 2 to SignIn
                            3. Press 3 to Write a post
                            4. Press 4 to message a friend
                            5. Press any other key to exit""")  
        
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()

    def signup(self):
        email = input("enter your email here ->")
        pwd = input("set your password here ->")
        self.username = email
        self.password = pwd
        print("You have successfully signed up !!")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == '' and self.password == '':
            print("Please sign up first by pressing 1 in the main menu")
        else:
            uname = input("enter your email/username here ->")
            pwd = input("enter your password here ->")
            if self.username == uname and self.password == pwd:
                print("You have signed in successfully !!")
                self.loggedin = True    
            else:
                print("please input correct credentials.")
        
        print("\n")
        self.menu()

obj = chatbook()
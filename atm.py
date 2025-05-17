class Atm:
    def __init__(self):
        self.name = ""
        self.pin = 0
        self.amount = 0
        self.new_amount = 0
        self.withdrawed = 0
        self.transaction = 0
        self.new_pin = 0
        self.new_name = ""

        self.menu()

    def menu(self):
        user_input = int(input("""
                                    press 1 for register
                                    press 2 for login
                                    press 0 to exit

                                    """))

        if user_input == 1:
            self.register()

        elif user_input == 2:
            self.login()

        elif user_input == 0:
            print("Loged Out successfully")
            pass

        else:
            print("invalid entry...!")

    def userinfo(self):  # userinfo code ko repeat honay say rokay ga

        self.name = input("please enter your name: ").strip()
        self.pin = int(input("please enter your pin: "))

    def register(self):
        self.userinfo()

        if len(str(self.pin)) != 4:
            print("""   
                                    please enter alteast 4 valid digits
                                    zero before non-zero value is not acceptable!
                                    please re-enter your credientials
                                    
                                    """)

            self.register()
        else:
            print("""

                                    welcome to our Atm machine
                                    please signin to get more info..

                                    """)

            # yahan ma nay variable banay hain jis ko hum aagay comparision k leay use karain gay

            self.new_name = self.name
            self.new_pin = self.pin
            self.login()   # self.login() likhnay say program continue ho ga login section k leay

    def login(self):
        self.userinfo()

        if self.name == self.new_name and self.pin == self.new_pin:
            print("login successful....")
            self.inner_menu()
        else:
            print("invalid entery please try again!!")
            return f"{self.menu()}"

    def balance(self):
        print("your amount is: ", self.amount)
        self.inner_menu()

    # ye menu is laeay banayea ha, user ko bar bar har function ki access denay k leay
    def inner_menu(self):

        self.inner = int(input("""
                                    press 1 for balance
                                    press 2 to deposit
                                    press 3 to withdraw  
                                    press 0 to exit
                                    
                                    """))
        if self.inner == 1:
            self.balance()
        elif self.inner == 2:
            self.deposit()
        elif self.inner == 3:
            self.withdraw()
        elif self.inner == 0:
            print("Loged Out successfully")
            pass
        else:
            print("invalid entry..!")

    def deposit(self):
        self.new_amount = int(
            input("please enter your amount to deposit...: "))
        self.amount += self.new_amount
        print("your balance is: ", self.amount)
        self.inner_menu()

    def withdraw(self):

        self.transaction = int(input("enter your amount to withdraw: "))

        if self.amount - self.transaction < 500:
            print("""
                                    insufficient balance :( 
                                    your balance shoukd be atleast 500 to play with...
                                    
                                    """)

        elif self.amount > self.transaction:
            self.amount = self.amount - self.transaction
            print("transaction sucessfull! ", self.transaction,
                  " and your remaining amount is: ", self.amount)
        else:
            print("insufficient balance :( deposit for better experience")

        self.inner_menu()


a = Atm()
b = Atm()

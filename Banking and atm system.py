class User:
    def __init__(self,name,age,gender,phonenumber,dob):
        self.name=name
        self.age=age
        self.gender=gender
        self.phone=phonenumber
        self.dob=dob
    def user_details(self):
        print('''USER DETAILS ARE :''')
        print()
        print("Name=",self.name)
        print("Age=",self.age)
        print("Gender=", self.gender)
        print("Phone Number", self.phone)
        print("Date Birth=", self.dob)

class Bank(User):
    def __init__(self,name,age,gender,phonenumber,dob):
        super().__init__(name,age,gender,phonenumber,dob)
        self.balance = 0
    def deposit(self,de):
        self.de=de
        self.balance=self.balance+self.de
        print("you deposit",self.de,"rupees")
        print("your updated balance after depodit is:",self.balance,"rupees")
    def withdraw(self,wi):
        self.wi=wi
        if(self.wi>self.balance):
            print("ERROE! you donot have sufficient amount.You have only:",self.balance,"rupees")
        else:
            self.balance=self.balance-self.wi
            print("you withdraw ",self.wi,"rupees")
            print("your updated balance after withdarw is ",self.balance,"rupees")
u=User("nav",23,"female",7986384623,"11-june-1998")
u.user_details()
b=Bank("nav",23,"female",7986384623,"11-june-1998")
b.deposit(1000)
b.withdraw(400)
b.deposit(500)
b.withdraw(1500)


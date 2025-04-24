class Bank:
    bank_name = "Default Bank"  

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name  

    def display(self):
        print("*" * 35)
        print("     💰 Bank Account Details 💰     ")
        print("*" * 35)
        print(f"Account Holder : {self.account_holder.title()}")
        print(f"Bank Name      : {Bank.bank_name}")
        print("*" * 35)


cust1 = Bank("bilal hussain")
cust2 = Bank("nouman")

cust1.display()
cust2.display()

Bank.change_bank_name("HBL Bank")

cust1.display()
cust2.display()

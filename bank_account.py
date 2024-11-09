class AccountDB:
    def __init__(self):
        self.accounts = []

    def insert(self, account):
        index = self.__find_account_index(account.account_number)
        if index == -1:
            self.accounts.append(account)
        else:
            print(account, "Duplicated account; nothing to be inserted")

    def delete_account(self, account_number):
        index = self.__find_account_index(account_number)
        if index != -1:
            print("Deleting account:", self.accounts[index])
            del self.accounts[index]
        else:
            print(account_number, "Invalid account number; nothing to be deleted.")

    def __find_account_index(self, account_number):
        for i in range(len(self.accounts)):
            if self.accounts[i].account_number == account_number:
                return i
        return -1

    def search_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return null_account

    def __str__(self):
        accounts_str = ''
        for account in self.accounts:
            accounts_str += str(account) + ", "
        return accounts_str


##############
class Account:
    def __init__(self, account_number, account_type, account_name, balance):
        self.account_number = account_number
        self.account_type = account_type
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount

    def __str__(self):
        return '{' + str(self.account_number) + ',' + str(self.account_type) + ',' + str(self.account_name) + ',' + str(
            self.balance) + '}'


############################################################
null_account = Account("Null", "any", "Null", 0)
account1 = Account("0000", "saving", "David Patterson", 1000)
account2 = Account("0001", "checking", "John Hennessy", 2000)
account3 = Account("0003", "saving", "Mark Hill", 3000)
account4 = Account("0004", "saving", "David Wood", 4000)
account5 = Account("0004", "saving", "David Wood", 4000)

my_account_db = AccountDB()
my_account_db.insert(account1)
my_account_db.insert(account2)
my_account_db.insert(account3)
my_account_db.insert(account4)
my_account_db.insert(account5)
print(my_account_db)

my_account_db.search_account("0003").deposit(50)
print(my_account_db)

my_account_db.search_account("0003").withdraw(100)
print(my_account_db)

my_account_db.search_account("0010").deposit(50)
print(my_account_db)

my_account_db.delete_account("0010")
print(my_account_db)

my_account_db.delete_account("0004")
print(my_account_db)

class Customer:
    last_id = 0

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        Customer.last_id += 1
        self.id = Customer.last_id

    def __repr__(self):
        return f'Customer[{self.id}, {self.firstname}, {self.lastname}]'

#AccountTransaction
class AccountTransaction:
    transaction_id = 1

    def __init__(self, transaction_type, amount):
        self.transaction_id = AccountTransaction.transaction_id
        AccountTransaction.transaction_id += 1
        self.transaction_type = transaction_type  # 'Deposit' or 'Charge'
        self.amount = amount

    def __repr__(self):
        return f'AccountTransaction[{self.transaction_id}, {self.transaction_type}, {self.amount}]'


class Account:
    last_id = 1000

    def __init__(self, customer):
        self.customer = customer
        Account.last_id += 1
        self.id = Account.last_id
        self._balance = 0
        self.transactions = [] # List to store transactions

    # Finish the implementation of the deposit and charge methods
    def deposit(self, amount):
        #Checks if amount is an instance of either int or float or a subclass thereof.
        # Validation
        if not isinstance(amount, (int, float)) or amount < 0:
            raise InvalidAmountException(f'Amount is invalid: {amount}')

        # Perform deposit
        self._balance += amount

        # Create and add a new transaction
        transaction = AccountTransaction('Deposit', amount)
        self.transactions.append(transaction)

    def charge(self, amount):
        # Validation
        if not isinstance(amount, (int, float)) or amount < 0:
            raise InvalidAmountException(f'Amount is invalid: {amount}')
        # Check if there is enough balance to perform the charge
        if self._balance < amount:
            raise InsufficientFundsException('Insufficient funds for the charge')
        # Perform charge
        self._balance -= amount
        # Create and add a new transaction
        transaction = AccountTransaction('Charge', amount)
        self.transactions.append(transaction)

    def get_transaction_history(self):
        return self.transactions # Retrieve the full historical report of transactions

    def __repr__(self):
        return f'Account[{self.id}, {self.customer.lastname}, {self._balance}]'


class Bank:
    def __init__(self):
        self.customer_list = []
        self.account_list = []

    def create_customer(self, firstname, lastname):
        c = Customer(firstname, lastname)
        self.customer_list.append(c)
        return c

    def create_account(self, customer):
        a = Account(customer)
        self.account_list.append(a)
        return a

    # Implement the transfer(...) in Bank
    def transfer(self, from_account_id, to_account_id, amount):
        # Validate input parameters
        if not isinstance(from_account_id, int) or not isinstance(to_account_id, int) or not isinstance(amount, (int, float)):
            raise InvalidTransferParametersException("Invalid transfer parameters")

        # Find "from" and "to" accounts based on the provided account ids
        from_account = self.find_account(from_account_id)
        to_account = self.find_account(to_account_id)

        # Check if both accounts are found
        if not from_account:
            raise ValueError(f'Account with ID {from_account_id} not found')
        if not to_account:
            raise ValueError(f'Account with ID {to_account_id} not found')

        # Check if the "from" account has sufficient funds
        if from_account._balance < amount:
            raise InsufficientFundsException("Insufficient funds for the transfer")

        # Perform the transfer
        from_account.charge(amount)
        to_account.deposit(amount)

    def find_account(self, account_id):
        for account in self.account_list:
            if account.id == account_id:
                return account
        return None

    def __repr__(self):
        return f'Bank[{self.customer_list}; {self.account_list}]'


class BankException(Exception):
    pass

class InsufficientFundsException(BankException):
    pass

class InvalidAmountException(BankException):
    pass

class InvalidTransferParametersException(BankException):
    pass

class ValueError(BankException):
    pass

bank = Bank()
print('--------#1. Create new customers and accounts:')
c = bank.create_customer('John', 'Brown')
print(c)
a = bank.create_account(c)
a2 = bank.create_account(c)
print(a)

c2 = bank.create_customer('Anne', 'Smith')
a3 = bank.create_account(c2)
print(bank)

print('-----#2. Find account')
a5=6
print(bank.find_account(a.id))
print(bank.find_account(a3))
print(bank.find_account(a5))

print('-----#3. Examples of Insufficient funds and Amount is invalid')
try:
    a2.charge(70)
except BankException as ie:
    print(f'Something went wrong {ie}')
#####################
try:
    a.deposit(330)
    a.charge(30)
    a2.deposit(50)
    a3.deposit(-100)
except BankException as ie:
    print(f'Something went wrong {ie}')
#except (InvalidAmountException, InsufficientFundsException) as ie:
#    print(f'Something went wrong {ie}')
except Exception as e:
    print(f'Exception was thrown: {e}')
else:
    print('Run it when no exception occured')
finally:
    print('This was run at the end')

#Print updated transaction history for account
print('---#4. Transaction History')
print("Transaction History for Account a:")
for transaction in a.get_transaction_history():
    print(transaction)

print("Transaction History for Account a2:")
for transaction in a2.get_transaction_history():
    print(transaction)

# Print account information after transactions
print("---#5. Account Information after Transactions:")
print(a)
print(a2)
print(a3)
#####################
print('-----#6. Transfering from account to account')
print("--- Examples for some errors")
#Example1
try:
    bank.transfer(a.id, a2.id, 400)
except BankException as ie:
    print(f'Something went wrong: {ie}')

#Example2
try:
    bank.transfer(a.id, a, 400)
except BankException as ie:
    print(f'Something went wrong: {ie}')

#Example3
a6=50
try:
    bank.transfer(a.id, a6, 400)
except BankException as ie:
    print(f'Something went wrong: {ie}')

print('--- Examples of transfering 20.5 from account a to account a2')
try:
    bank.transfer(a.id, a2.id, 20.5)
except BankException as ie:
    print(f'Something went wrong: {ie}')

print("--- Transaction History for Account a:")
for transaction in a.get_transaction_history():
    print(transaction)
print("--- Transaction History for Account a2:")
for transaction in a2.get_transaction_history():
    print(transaction)
print("---Account Information after Transactions:")
print(a)
print(a2)
print('--------')



class Account:
    def __init__(self):
        self.deposits = []
        self.withdrawals = []
        self.loan_balance = 0

    def check_balance(self):
        total_deposits = sum(transaction['amount'] for transaction in self.deposits)
        total_withdrawals = sum(transaction['amount'] for transaction in self.withdrawals)
        return total_deposits - total_withdrawals

    def deposit(self, amount):
        transaction = {
            "amount": amount,
            "narration": "deposit"
        }
        self.deposits.append(transaction)

    def withdrawal(self, amount):
        transaction = {
            "amount": amount,
            "narration": "withdrawal"
        }
        self.withdrawals.append(transaction)

    def print_statement(self):
        transactions = self.deposits + self.withdrawals
        for transaction in transactions:
            print(f"{transaction['narration']} - {transaction['amount']}")

    def borrow_loan(self, amount):
        if self.loan_balance == 0 and amount > 100 and len(self.deposits) >= 10:
            total_deposits = sum(transaction['amount'] for transaction in self.deposits)
            if amount <= total_deposits / 3:
                self.loan_balance = amount
                print("Loan approved!")
            else:
                print("Loan amount exceeds 1/3 of total deposits.")
        else:
            print("Loan request denied.")

    def repay_loan(self, amount):
        if amount > self.loan_balance:
            overpayment = amount - self.loan_balance
            self.deposit(overpayment)
            self.loan_balance = 0
            print("Loan fully repaid. Overpayment deposited to account.")
        else:
            self.loan_balance -= amount
            print("Loan partially repaid.")

    def transfer(self, amount, other_account):
        if amount <= self.check_balance():
            self.withdrawal(amount)
            other_account.deposit(amount)
            print("Transfer successful.")
        else:
            print("Insufficient funds for transfer.")



my_account = Account()


my_account.deposit(1000)
my_account.deposit(2000)


my_account.withdrawal(500)

my_account.print_statement()

my_account = Account()


my_account.deposit(1000)
my_account.deposit(2000)


my_account.withdrawal(500)


my_account.print_statement()


my_account.borrow_loan(500)


my_account.repay_loan(200)


other_account = Account()
my_account.transfer(300, other_account)

my_account.borrow_loan(500)

my_account.repay_loan(200)

other_account = Account()
my_account.transfer(300, other_account)





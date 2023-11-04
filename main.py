import csv

class Bank:
    def __init__(self, pwd, acc, balance):
        self.pwd = pwd
        self.acc = acc
        self.balance = balance
        self.transaction_history = []

    def operation(self, accounts):
        while True:
            print('Please select an operation:')
            print('1. Check your Bank Balance')
            print('2. Withdraw')
            print('3. Deposit')
            print('4. Transfer Money')
            print('5. Show Last 5 Transactions')
            print('6. Exit')
            
            choice = int(input('Enter your choice: '))
            
            if choice == 1:
                print(f'Current Balance: {self.balance}')
            elif choice == 2:
                amount = float(input('Please Enter the Amount: '))
                self.withdraw(amount)
            elif choice == 3:
                amount = float(input('Please Enter the Amount: '))
                self.deposit(amount)
            elif choice == 4:
                self.transfer_money(accounts)
            elif choice == 5:
                self.show_last_5_transactions()
            elif choice == 6:
                print('Thank you for banking with us. Have a good day...')
                break
            else:
                print('Please select a valid option')

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient Balance...')
        else:
            self.balance -= amount
            self.transaction_history.append(f'Withdrawal of {amount}')
            print('Withdrawal Successful')
            print(f'Updated balance: {self.balance}')

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f'Deposit of {amount}')
        print('Deposit Successful')
        print(f'Updated Balance: {self.balance}')

    def transfer_money(self, accounts):
        print('Enter details of the account you want to transfer to:')
        account_number = input('Enter the account number: ')
        amount = float(input('Enter the amount to transfer: '))

        sender = None
        receiver = None

        for acc in accounts:
            if acc.acc == self.acc:
                sender = acc
            if acc.acc == account_number:
                receiver = acc

        if sender and receiver:
            if amount > sender.balance:
                print("Insufficient funds for the transfer.")
            else:
                sender.balance -= amount
                receiver.balance += amount
                sender.transaction_history.append(f'Transfer of {amount} to account {receiver.acc}')
                receiver.transaction_history.append(f'Received transfer of {amount} from account {sender.acc}')
                print("Transfer successful.")
        else:
            print("Accounts not found. Please check the account numbers.")

    def show_last_5_transactions(self):
        if not self.transaction_history:
            print("No transaction history yet.")
        else:
            print("Last 5 Transactions:")
            for transaction in self.transaction_history[-5:]:
                print(transaction)

def create_account():
    pwd = input('Enter a password: ')
    acc = input('Enter account number: ')
    balance = float(input('Enter initial balance: '))
    return Bank(pwd, acc, balance)

def save_account_details(accounts):
    with open('account_details.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for account in accounts:
            writer.writerow([account.pwd, account.acc, account.balance, '|'.join(account.transaction_history)])


def load_account_details(account_number):
    try:
        with open('account_details.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[1] == account_number:
                    return Bank(row[0], row[1], float(row[2]))
    except FileNotFoundError:
        return None

def main():
    accounts = []  # Initialize an empty list to hold accounts

    # Load existing accounts from the CSV file
    with open('account_details.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            accounts.append(Bank(row[0], row[1], float(row[2])))

    print('Welcome.')
    print('1. Login to your bank account')
    print('2. Create an account')
    choice = int(input('Enter your choice: '))
    
    if choice == 1:
        id = input('Please enter your account number: ')
        passw = input('Enter your password: ')
        
        current_acc = None
        for acc in accounts:
            if acc.acc == id and acc.pwd == passw:
                current_acc = acc
                break
        
        if current_acc:
            current_acc.operation(accounts)  # Pass 'accounts' to the operation method
            save_account_details(accounts)  # Save all accounts back to the CSV file
        else:
            print('Invalid Credentials. Please try again...')
    
    elif choice == 2:
        new_acc = create_account()
        accounts.append(new_acc)
        save_account_details(accounts)  # Save all accounts back to the CSV file
        new_acc.operation(accounts)  # Pass 'accounts' to the operation method
    else:
        print('Please select a valid option')

if __name__ == "__main__":
    main()
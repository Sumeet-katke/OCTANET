Bank Account Management System
This Python program simulates a simple bank account management system allowing users to create bank accounts, log in, and perform various banking operations such as checking balance, withdrawing money, depositing money, transferring funds between accounts, and viewing transaction history.

How to Use
Prerequisites
Python 3.x installed
Steps to run the program
Download the code:

Save the provided Python code in a file (e.g., bank_system.py).
Run the program:

Open a terminal or command prompt.
Navigate to the directory where the bank_system.py file is saved.
Execute the program by running python bank_system.py.
Follow the prompts:

Upon running the program, follow the instructions displayed on the console:
You can either choose to log in with an existing account or create a new account.
For an existing account, enter the account number and password.
For a new account, enter a password, account number, and an initial balance.
Perform banking operations:

After logging in or creating an account, you can select various operations:
Check account balance.
Withdraw money.
Deposit money.
Transfer money to another account.
View the last 5 transactions.
Exit the program.
Save changes:

Any changes made to the accounts (creation, transactions) will be saved to the account_details.csv file.
Files
bank_system.py
This file contains the Python code for the bank account management system. It includes classes and functions to handle account operations, read/write account data to a CSV file, and the main program to execute the banking functionalities.

account_details.csv
This CSV file stores account information:

Password
Account number
Account balance
Transaction history (in a pipe-separated format)
Notes
The program utilizes CSV file handling to read and write account details. Ensure the account_details.csv file is present and accessible in the same directory as the Python script.

# local imports
from finance import get_current_bal, deposit, update_transactions, transactions

counter = 1


def menu(user):
    print("1: Check Balance\r\n2: Deposit\r\n3: Add transaction\r\n4: View Transactions\r\nPress Enter To exit...")
    opt = input("> ")

    if opt == "1":
        get_current_bal(user)

        menu(user)
    
    elif opt == "2":
        amt = float(input("Ammount to deposit: "))
        deposit(user, amt)


        menu(user)
    
    elif opt == "3":
        credit = float(input("Transaction Ammount: "))
        transaction_id = int(input("Transction ID: "))

        update_transactions(user, credit, transaction_id)

        menu(user)

    elif opt == "4":
        transactions(user)

        menu(user)
    else:
        exit

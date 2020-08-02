
# global imports

from getpass import getpass
import sqlite3
import argparse
import os
import hashlib
import random

# local imports
from auth import create_user, login
from tools import counter, menu

from finance import get_current_bal, deposit, transactions, update_transactions


def main():
    already_user = input("Do you have an account? (Y/n) ")
    user = str()
    
    if already_user == 'n':
        create_user()
    else:
        user = login(counter)

        if user == None:
            print("Authentication failed")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Welcome, ", user, "\r\n")
    
    menu(user)
    
    
        


try:
    main()
except KeyboardInterrupt:
    print("\r\nExiting...")




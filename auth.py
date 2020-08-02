from getpass import getpass
import sqlite3
import argparse
import os
import hashlib
import random
import time

# local imports

from close_db import close_db
from tools import counter


def create_user():
    os.system('cls' if os.name == 'nt' else 'clear')
    conn = sqlite3.connect('data/usr.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users 
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     username TEXT, password_hash TEXT)''')

    username = input("Username: ")
    password = getpass('> ')

    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

    storage = salt + key 

    conn.execute('INSERT INTO users VALUES (?, ?, ?)', 
    (random.randint(1000, 9999), username, storage))

    close_db(conn)

    login(counter)
    


def login(counter):
        os.system('cls' if os.name == 'nt' else 'clear')
        data = list()
        conn = sqlite3.connect('data/usr.db')
        c = conn.cursor()
        username = input("Username: ")
        password_to_check = getpass('> ')
        try:
            c.execute('SELECT * FROM users WHERE username=?', (username, ))
            rows = c.fetchone()

            for row in rows:
                data.append(row)


            salt_from_storage = data[2][:32]
            key_from_storage = data[2][32:]
        except TypeError:
            print("User not found")
            return login(counter)

        except :
            print('test')
        

        # verification
        new_key = hashlib.pbkdf2_hmac(
            'sha256',
            password_to_check.encode('utf-8'), # Convert the password to bytes
            salt_from_storage, 
            100000
        )

        
        if counter < 4 and counter > 0:
            if new_key == key_from_storage:
                return data[1]
            else:
                print("Login failed, try again ", counter, " attempts remaining")
                counter = counter - 1
                login(counter)

        close_db(conn)
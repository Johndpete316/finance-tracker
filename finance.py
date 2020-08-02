import sqlite3
import random

# local imports 
from close_db import close_db

def get_current_bal(user):
    data = list()
    conn = sqlite3.connect(f'data/{user}.db')
    c = conn.cursor()
    try:
        c.execute(f'''CREATE TABLE IF NOT EXISTS {user} (id INTEGER PRIMARY KEY AUTOINCREMENT, balance REAL, connections INT)''')
        c.execute(f'SELECT * FROM {user}')
        rows = c.fetchone()

        for row in rows:
            data.append(row)

        print(f'Account balance for {user}: {data[1]}')

        c.execute(f'UPDATE {user} SET connections=? WHERE id=0', (data[2] + 1,) )
    except:
        c.execute(f'''CREATE TABLE IF NOT EXISTS {user} (id INTEGER PRIMARY KEY AUTOINCREMENT, balance REAL, connections INT)''')
        print("No deposits made.")
    
    input("press enter to continue...")
    close_db(conn)


def deposit(user, amt):
    data = list()
    conn = sqlite3.connect(f'data/{user}.db')
    c = conn.cursor()

    c.execute(f'''CREATE TABLE IF NOT EXISTS {user} (id INTEGER PRIMARY KEY AUTOINCREMENT, balance REAL, connections INT)''')
    try:
        c.execute(f'SELECT * FROM {user}')
        rows = c.fetchone()

        for row in rows:
            data.append(row)
        
        print(f'Account balance for {user}: {data[1] + amt}')
        c.execute(f'UPDATE {user} SET balance=?, connections=? WHERE id=0', (data[1] + amt, data[2] + 1, ))

    except:
        print(f'Account balance for {user}: {amt}')
        c.execute(f'INSERT INTO {user} VALUES (?, ?, ?)', (0, amt, 1))


    input("press enter to continue...")
    close_db(conn)

def transactions(user):
    data = list()
    conn = sqlite3.connect(f'data/{user}.db')
    c = conn.cursor()

    c.execute(f'CREATE TABLE IF NOT EXISTS transactions (id INTEGER PRIMARY KEY AUTOINCREMENT, credit REAL, trans_id INTEGER)')
    c.execute(f'SELECT * FROM transactions')
    rows = c.fetchall()

    for row in rows:
        data.append(row)

    i = 0
    while i < len(data):
        print("================================")
        print(f"| {data[i][0]} | {data[i][1]} | {data[i][2]} |")

        i += 1
    input("press enter to continue...")

    close_db(conn)

def update_transactions(user, credit, transaction_id):
    conn = sqlite3.connect(f'data/{user}.db')
    c = conn.cursor()

    data = list()
    table_id = random.randint(1000, 9999)

    c.execute(f'CREATE TABLE IF NOT EXISTS transactions (id INTEGER PRIMARY KEY AUTOINCREMENT, credit REAL, trans_id INTEGER)')
    c.execute(f'INSERT INTO transactions VALUES (?, ?, ?)', (table_id, credit, transaction_id))
    
    c.execute(f'SELECT * FROM transactions')
    rows = c.fetchall()

    for row in rows:
        data.append(row)

    i = 0
    while i < len(data):
        print("====================")
        print(f"| {data[i][0]} | {data[i][1]} | {data[i][2]} |")

        i += 1

    input("press enter to continue...")
    close_db(conn)

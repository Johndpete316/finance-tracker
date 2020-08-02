import os

def close_db(conn):
    os.system('cls' if os.name == 'nt' else 'clear')

    conn.commit()
    conn.close()
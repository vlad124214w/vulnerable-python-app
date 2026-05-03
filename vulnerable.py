import subprocess
import sqlite3
import os

# УЯЗВИМОСТЬ 1: Command Injection
def ping_host(user_input):
    # shell=True + прямая подстановка → RCE
    subprocess.call(f"ping -c 1 {user_input}", shell=True)

# УЯЗВИМОСТЬ 2: SQL Injection
def get_user_by_name(username):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    # Прямая конкатенация → SQLi
    query = f"SELECT * FROM users WHERE name = '{username}'"
    return cursor.execute(query).fetchall()

# УЯЗВИМОСТЬ 3: Hardcoded credentials


# УЯЗВИМОСТЬ 4: Path Traversal
def read_file(filename):
    # user_input может быть ../../../etc/passwd
    with open(f"/var/www/uploads/{filename}", "r") as f:
        return f.read()

# УЯЗВИМОСТЬ 5: XSS (в веб-контексте)
def render_user_input(user_input):
    # Без экранирования → XSS
    return f"<div class='message'>{user_input}</div>"

if __name__ == "__main__":
    user_input = input("Enter IP or domain: ")
    ping_host(user_input)
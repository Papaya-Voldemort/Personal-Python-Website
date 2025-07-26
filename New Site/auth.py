from pywebio.output import popup, close_popup, put_text, clear
from pywebio.input import input_group, input
from tinydb import TinyDB, Query
import bcrypt
import time
from datetime import datetime

users = TinyDB('users.json')
stats = TinyDB('stats.json')

def add_stat(stat_name, increment=1):
    """Add or increment a stat - moved here to avoid circular import"""
    # Check if stat already exists
    existing_stat = stats.search(Query().stat_name == stat_name)

    if existing_stat:
        # Update existing stat by incrementing the value
        current_value = existing_stat[0].get('value', 0)
        stats.update({'value': current_value + increment, 'timestamp': datetime.now().isoformat()},
                     Query().stat_name == stat_name)
    else:
        # Create new stat if it doesn't exist
        stats.insert({'stat_name': stat_name, 'value': increment, 'timestamp': datetime.now().isoformat()})

def login():
    user_info = input_group("Login", [
        input("Username", name="username"),
        input("Password", name="password", type="password")
    ])
    User = Query()
    # Check if the user exists
    user = users.search(User.username == user_info['username'])
    if not user:
        popup("Error", "Username does not exist. Please sign up first.")
        return
    user = user[0]  # Get the first matching user
    # Verify the password
    if not bcrypt.checkpw(user_info['password'].encode('utf-8'), user['password'].encode('utf-8')):
        popup("Error", "Incorrect password. Please try again.")
        return
    # Successful login
    clear()
    put_text(f"Welcome back, {user_info['username']}!")
    add_stat('total_logins')  # Increment login count stat
    time.sleep(1.5)
    clear()
    # Import utils here to avoid circular import
    import utils
    utils.dashboard()  # Redirect to the main menu after login

def signup():
    user_info = input_group("Sign Up", [
        input("Username", name="username"),
        input("Password", name="password", type="password"),
        input("Email", name="email")
    ])

    # Check if the username already exists
    User = Query()
    if users.search(User.username == user_info['username']):
        popup("Error", "Username already exists. Please choose a different username.")
        return

    # Hash the password
    hashed_password = bcrypt.hashpw(user_info['password'].encode('utf-8'), bcrypt.gensalt())

    # Store the user information
    users.insert({
        'username': user_info['username'],
        'theme': 'default',
        'password': hashed_password.decode('utf-8'),
        'email': user_info['email']
    })

    clear()
    put_text(f"User {user_info['username']} signed up successfully!")
    time.sleep(3)
    clear()
    # Import utils here to avoid circular import
    import utils
    utils.main_menu()  # Redirect to the main menu after signup

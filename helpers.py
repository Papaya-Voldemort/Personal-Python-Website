from pywebio.input import input, input_group, PASSWORD, actions
from pywebio.output import put_text
from pywebio import start_server
from tinydb import TinyDB, Query

def sign_up(users):
    data = input_group("Sign Up", [
        input("Choose a Username", name='username'),
        input("Choose a Password", type=PASSWORD, name='password')
    ])
    if users.search(Query().username == data['username']):
        put_text("Username already exists. Please choose a different username.")
        sign_up(users)  # Prompt the user to sign up again
    else:
        users.insert({'username': data['username'], 'password': data['password']})
        put_text(f"Account created successfully! You can now log in, {data['username']}.")

def login(users):
    data = input_group("Login", [
        input("Username", name='username'),
        input("Password", type=PASSWORD, name='password')
    ])
    if users.search((Query().username == data['username']) & (Query().password == data['password'])):
        put_text(f"Welcome back, {data['username']}!")
    else:
        put_text("Invalid username or password. Please try again.")
        login(users)  # Prompt the user to log in again

def view_dashboard():
    put_text("This is the dashboard. More features coming soon!")
from pywebio import start_server
from pywebio.output import put_text, put_tabs, put_markdown, put_buttons
from pywebio.input import input
import auth

def main_menu():
    put_tabs([
        {
            'title': 'Logins',
            'content': [
                put_markdown("## Welcome, please log in to continue or sign up."),
                put_buttons(['Login'], onclick=lambda btn: auth.login()),
            ]
        },
        {
            'title': 'Sign Up',
            'content': [
                put_markdown("## Welcome, please sign up to continue."),
                put_buttons(['Sign Up'], onclick=lambda btn: auth.signup()),

            ]
        },
    ])

def dashboard():
    print("Make this later")
    #TODO make dash
    #TODO push code to repository

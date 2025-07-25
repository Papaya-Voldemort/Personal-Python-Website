from pywebio import start_server
from pywebio.output import put_text, put_tabs, put_markdown, put_buttons, clear, use_scope, put_html, put_scope
from pywebio.input import input, NUMBER
import auth
import time
from datetime import datetime, timedelta
import threading

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
    def timer():
        with use_scope('countdown', clear=True):
            put_markdown("## SoM Countdown")
            with use_scope('timer', clear=True):
                end_time = datetime(2025, 8, 31)

                while True:
                    current_time = datetime.now()
                    seconds_until_end = int((end_time - current_time).total_seconds())

                    if seconds_until_end <= 0:
                        put_text("SoM has ended!")
                        break

                    put_text(f"Seconds until SoM ends: {seconds_until_end}")
                    put_text(f"Minutes until SoM ends: {seconds_until_end / 60:.1f}")
                    put_text(f"Hours until SoM ends: {seconds_until_end / 3600:.1f}")
                    put_text(f"That's approximately {seconds_until_end / 86400:.1f} days until SoM ends!")

                    time.sleep(1)  # Update every second
                    clear('timer')




    put_tabs([
        {
            'title': 'Dashboard',
            'content': put_text("Welcome to the dashboard! Here you can use all of the features of the site."
                                "\nJust click on one of the tabs to get started.")
        },
        {
            'title': 'SoM Countdown',
            'content': [
                put_text("This is the SoM Countdown tab. Here you can see the countdown to the end of SoM 2025."),
                put_buttons(['Start Countdown'], onclick=lambda btn: timer()),
            ]
        }
    ])

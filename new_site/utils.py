from pywebio.output import put_text, put_tabs, put_markdown, put_buttons, clear, use_scope, put_html, put_scope, put_table
from pywebio.input import input, NUMBER
import time
from datetime import datetime, timedelta
import threading
import new_site.AI as AI
import tinydb
import new_site.wifi_utils as wifi_utils

stats = tinydb.TinyDB('stats.json')


def main_menu():
    # Import auth here to avoid circular import
    import new_site.auth as auth

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

    def load_stats():
        clear('stats')
        with use_scope('stats', clear=True):
            put_markdown("## Stats")
            stats_data = stats.all()
            if not stats_data:
                put_text("No stats available.")
                return

            # Display stats as a table
            headers = ['Stat Name', 'Value', 'Last Updated']
            rows = [[stat['stat_name'], stat['value'], stat['timestamp']] for stat in stats_data]
            put_table([headers] + rows)

    clearable_scopes = ['countdown', 'timer', 'ai_quote', 'stats', 'wifi_speed_test']

    def clean_scopes():
        for scope in clearable_scopes:
            clear(scope)

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

    def ai_quote_generator():
        clear('ai_quote')
        with use_scope('ai_quote', clear=True):
            put_markdown(f"## AI Quote: ")
            quote = AI.generate_ai_quote()
            if quote.startswith("Error:"):
                put_text(quote)
                return
            else:
                # Import here to avoid circular import
                import new_site.auth as auth
                auth.add_stat('ai_quotes_generated')
            put_text(quote)

    put_tabs([
        {
            'title': 'Dashboard',
            'content': put_text("Welcome to the dashboard! Here you can use all of the features of the site."
                                "\nJust click on one of the tabs to get started."),
            #add clear stats
        },
        {
            'title': 'SoM Countdown',
            'content': [
                put_text("This is the SoM Countdown tab. Here you can see the countdown to the end of SoM 2025."),
                put_buttons(['Start Countdown'], onclick=lambda btn: (clean_scopes(), timer())),
            ]
        },
        {
            'title': 'AI Quote Generator',
            'content': [
                put_text("This is the AI Quote Generator tab. Here you can generate quotes using AI."),
                put_buttons(['Generate Quote'], onclick=lambda btn: (clean_scopes(), ai_quote_generator())),
            ]
        },
        {
            'title': 'Stats',
            'content': [
                put_text("This is the Stats tab. Here you can see some basic stats about the site."),
                put_buttons(['Load Stats'], onclick=lambda btn: (clean_scopes(), load_stats_with_increment())),
            ]
        },
        { 'title': 'Speed Test',
            'content': [
                put_text("This is the Speed Test tab. Here you can test your internet speed."),
                put_buttons(['Run Speed Test'], onclick=lambda btn: (clean_scopes(), wifi_utils.wifi_speed_test())),
            ]
        },
    ])


def load_stats_with_increment():
    """Helper function to increment stats and load them"""
    import new_site.auth as auth
    auth.add_stat('stats_page_views')

    clear('stats')
    with use_scope('stats', clear=True):
        put_markdown("## Stats")
        stats_data = stats.all()
        if not stats_data:
            put_text("No stats available.")
            return

        # Display stats as a table
        headers = ['Stat Name', 'Value', 'Last Updated']
        rows = [[stat['stat_name'], stat['value'], stat['timestamp']] for stat in stats_data]
        put_table([headers] + rows)

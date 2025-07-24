import pywebio.output
from pywebio.input import input, input_group, PASSWORD, actions, select
from pywebio.output import put_text, clear, put_info
from pywebio import start_server, session, config
from pywebio.session import run_js
from tinydb import TinyDB, Query
import time
import datetime
import time
import random

# Map of themes to Bootswatch URLs
BOOTSWATCH_THEMES = {
    "default": "https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css",
    "dark": "https://cdn.jsdelivr.net/npm/bootswatch@4.6.2/dist/darkly/bootstrap.min.css",
    "minty": "https://cdn.jsdelivr.net/npm/bootswatch@4.6.2/dist/minty/bootstrap.min.css",
    "yeti": "https://cdn.jsdelivr.net/npm/bootswatch@4.6.2/dist/yeti/bootstrap.min.css",
    "sketchy": "https://cdn.jsdelivr.net/npm/bootswatch@4.6.2/dist/sketchy/bootstrap.min.css",
    "sandstone": "https://cdn.jsdelivr.net/npm/bootswatch@4.6.2/dist/sandstone/bootstrap.min.css",
}


def aura_ranker():
    put_text("Aura Ranker")
    progress = 0.0
    pywebio.output.put_progressbar("loading_aura_ranker", progress, "Loading Aura Ranker")
    while progress < 1.0:
        progress += 0.1
        pywebio.output.set_progressbar("loading_aura_ranker", progress, "Loading Aura Ranker")
        time.sleep(1)
    put_text("Aura Ranker Loaded...")
    time.sleep(3)

    pywebio.output.popup("Aura Ranker", f"Your Aura is {random.randint(1, 100)}% nice!", "large", True)
    clear()

def apply_theme_live(theme):
    """Apply theme change immediately without page reload"""
    css_url = BOOTSWATCH_THEMES[theme]

    # Inject a new <link> tag for the chosen theme
    run_js(f"""
    (function() {{
        let existing = document.querySelector('link[rel=stylesheet][href*="bootstrap"]');
        if(existing) existing.remove();
        let link = document.createElement('link');
        link.rel = 'stylesheet';
        link.href = "{css_url}";
        document.head.appendChild(link);
    }})();
    """)

def load_user_theme(users, username):
    """Load and apply the user's saved theme"""
    user = users.search(Query().username == username)
    if user and 'theme' in user[0]:
        theme = user[0]['theme']
        apply_theme_live(theme)
        return theme
    else:
        # Apply default theme if no theme is saved
        apply_theme_live('default')
        return 'default'

def sign_up(users):
    data = input_group("Sign Up", [
        input("Choose a Username", name='username'),
        input("Choose a Password", type=PASSWORD, name='password')
    ])
    if users.search(Query().username == data['username']):
        put_text("Username already exists. Please choose a different username.")
        sign_up(users)
    else:
        users.insert({'username': data['username'], 'password': data['password'], 'theme': 'default'})
        put_text(f"Account created successfully! You can now log in, {data['username']}.")

def login(users):
    data = input_group("Login", [
        input("Username (use guest for testing)", name='username'),
        input("Password (use guest for testing)", type=PASSWORD, name='password')
    ])
    if users.search((Query().username == data['username']) & (Query().password == data['password'])):
        put_text(f"Welcome back, {data['username']}!")
        return data['username']
    else:
        put_text("Invalid username or password. Please try again.")
        return login(users)# Prompt the user to log in again

def view_dashboard(users, username):
    def set_user_theme(users, username, theme):
        User = Query()
        users.update({'theme': theme}, User.username == username)

    def countdown(seconds):
        for i in range(seconds, 0, -1):
            clear()
            put_text(f"Summer of Making ends in {i} seconds")
            time.sleep(1)
        clear()
        put_text("Time's up!")

    dashboard_options = input_group("Dashboard", [
        actions(name='Start', buttons=[{'label': 'Time until SoM end!', 'value': 'start'}]),
        actions(name='User_Settings', buttons=[{'label': 'User Settings', 'value': 'settings'}]),
        actions(name='Quotes', buttons=[{'label': 'Quotes', 'value': 'quotes'}]),
        actions(name='About_me', buttons=[{'label': 'About me', 'value': 'about'}]),
        actions(name="Aura_Ranker", buttons=[{'label': 'Aura Ranker', 'value': 'ranking'}]),
    ])

    if dashboard_options['Start'] == 'start':
        now = datetime.datetime.now()
        august_31 = datetime.datetime(now.year, 8, 31, 0, 0, 0)
        seconds_until_august_31 = int((august_31 - now).total_seconds())
        countdown(seconds_until_august_31)
    elif dashboard_options['User_Settings'] == 'settings':
        put_text("🎨 User Settings - Theme Selection")

        theme = select("Choose a theme:", list(BOOTSWATCH_THEMES.keys()))

        # Apply the theme immediately with live switching
        apply_theme_live(theme)

        # Save the theme preference to the database
        set_user_theme(users, username, theme)

        # Provide feedback to the user
        put_text(f"✅ Theme switched to: {theme.capitalize()}")
        put_text("Your theme preference has been saved!")
        time.sleep(3)
        clear()
        return "reset"

    elif dashboard_options['Quotes'] == 'quotes':
        print("No quotes yet!")
        #TODO add random quotes api



    elif dashboard_options['About_me'] == 'about':
        put_text("About me!")
        progress = 0.0
        pywebio.output.put_progressbar("loading", progress, None)
        while progress < 1.0:
            progress += 0.1
            pywebio.output.set_progressbar("loading", progress, None)
            time.sleep(1)
        clear()
        put_text("About me!")
        put_info("""
        I am a 15 year old boy who loves to code!\n
        My favorite language is Python because of its easy to learn structure and speed of development\n
        I recently discovered pywebio an amazing python web framework\n
        It makes development fast and easy!""")

    elif dashboard_options['Aura_Ranker'] == 'ranking':
        aura_ranker()
        return "reset"




    else:
        put_text("Invalid option. Please try again.")
        view_dashboard(users, username)

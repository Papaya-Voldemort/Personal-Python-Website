import time
import datetime
import random
import bcrypt

from tinydb import TinyDB, Query

from pywebio import start_server, session, config
from pywebio.input import input, input_group, PASSWORD, actions, select
from pywebio.output import (
    put_text, clear, put_info, put_tabs, put_buttons,
    put_markdown, put_progressbar, set_progressbar
)
from pywebio.session import run_js, run_async

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
        password = data['password'].encode('utf-8')
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        users.insert({'username': data['username'], 'password': hashed.decode('utf-8'), 'theme': 'default'})
        put_text(f"Account created successfully! You can now log in, {data['username']}.")

def login(users):
    data = input_group("Login", [
        input("Username (use guest for testing)", name='username'),
        input("Password (use guest for testing)", type=PASSWORD, name='password')
    ])
    user = users.search(Query().username == data['username'])
    if user:
        stored_hash = user[0]['password'].encode('utf-8')
        if bcrypt.checkpw(data['password'].encode('utf-8'), stored_hash):
            put_text(f"Welcome back, {data['username']}!")
            return data['username']
    put_text("Invalid username or password. Please try again.")
    return login(users)

from pywebio.output import put_tabs, put_text, put_buttons, put_info, put_progressbar, set_progressbar, clear
from pywebio.input import select
import time, datetime

def view_dashboard(users, username):
    def set_user_theme(users, username, theme):
        User = Query()
        users.update({'theme': theme}, User.username == username)

    def tab_som_timer():
        now = datetime.datetime.now()
        august_31 = datetime.datetime(now.year, 8, 31)
        seconds = int((august_31 - now).total_seconds())
        put_text(f"⏳ Summer of Making ends in {seconds:,} seconds!")

    def tab_user_settings():
        put_text("🎨 User Settings - Theme Selection")
        theme = select("Choose a theme:", list(BOOTSWATCH_THEMES.keys()))
        apply_theme_live(theme)
        set_user_theme(users, username, theme)
        put_text(f"✅ Theme switched to: {theme.capitalize()}")
        put_text("Your theme preference has been saved!")

    def tab_quotes():
        put_text("📜 Quotes")
        put_text("No quotes yet! (To be implemented)")

    def tab_about_me():
        put_text("👤 About Me Loading...")
        put_progressbar("loading", 0)
        for i in range(10):
            time.sleep(0.1)
            set_progressbar("loading", (i+1)/10)
        clear()
        put_text("👤 About Me")
        put_info("""
        I am a 15-year-old who loves to code!  
        My favorite language is Python because of its clear structure and fast development time.  
        I recently discovered PyWebIO — an amazing Python web framework that makes development quick and fun!
        """)

    def tab_aura_ranker():
        aura_ranker()  # Assuming defined elsewhere

    # 🧠 True lazy tabs — use lambdas so they don’t all run immediately!
    put_tabs([
        {'title': 'SoM Countdown', 'content': lambda: tab_som_timer()},
        {'title': 'User Settings', 'content': lambda: tab_user_settings()},
        {'title': 'Quotes', 'content': lambda: tab_quotes()},
        {'title': 'About Me', 'content': lambda: tab_about_me()},
        {'title': 'Aura Ranker', 'content': lambda: tab_aura_ranker()},
    ])


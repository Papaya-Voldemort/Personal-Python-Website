import pywebio
from pywebio.input import select
from pywebio.output import put_html, put_buttons, put_text, clear
from pywebio.session import run_js
from pywebio import start_server

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
    pywebio.output.put_loading("grow", "primary", "Test")

def main():
    put_text("🎨 Pick your theme from the dropdown below:")

    theme = select("Choose a theme:", list(BOOTSWATCH_THEMES.keys()))

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

    clear()
    put_text(f"✅ Theme switched to: {theme.capitalize()}")


if __name__ == '__main__':
    start_server(main, port=8080)

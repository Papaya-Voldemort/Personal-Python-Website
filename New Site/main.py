from pywebio import start_server
from pywebio.output import put_text, put_tabs, put_markdown, put_buttons
from pywebio.input import input
import auth
import utils

def main():
    utils.main_menu()

if __name__ == '__main__':
    start_server(main, port=8080)
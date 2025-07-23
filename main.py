from pywebio.input import input, input_group, PASSWORD, actions
from pywebio.output import put_text
from pywebio import start_server
from tinydb import TinyDB
from tinydb.storages import JSONStorage
import json
from helpers import sign_up, login

class PrettyJSONStorage(JSONStorage):
    def __init__(self, path, **kwargs):
        super().__init__(path, **kwargs)
        self._filename = path
    def write(self, data):
        with open(self._filename, 'w') as f:
            json.dump(data, f, indent=4)

users = TinyDB('users.json', storage=PrettyJSONStorage)

def app():
    has_account = input_group("Options", [
        actions(name='Login', buttons=[{'label': 'Login', 'value': 'login'}]),
        actions(name='Sign_Up', buttons=[{'label': 'Sign Up', 'value': 'sign_up'}])
    ])
    if has_account['Login'] == 'login':
        login(users)
    elif has_account['Sign_Up'] == 'sign_up':
        sign_up(users)

if __name__ == '__main__':
    start_server(app, port=8080, cdn=True)

import pywebio
from pywebio.input import input, input_group, PASSWORD, actions
from pywebio.output import put_text
from pywebio import start_server, config
from tinydb import TinyDB, Query
from tinydb.storages import JSONStorage
import json
from helpers import sign_up, login, view_dashboard




class PrettyJSONStorage(JSONStorage):
    def __init__(self, path, **kwargs):
        super().__init__(path, **kwargs)
        self._filename = path
    def write(self, data):
        with open(self._filename, 'w') as f:
            json.dump(data, f, indent=4)

users = TinyDB('users.json', storage=PrettyJSONStorage)

def app():
    pywebio.output.popup("Welcome!", "Welcome! Feel free to test things out! \n"
                                                  "I am not sure about my hosting so it might break!", "large", True)


    has_account = input_group("Options", [
        actions(name='Login', buttons=[{'label': 'Login', 'value': 'login'}]),
        actions(name='Sign_Up', buttons=[{'label': 'Sign Up', 'value': 'sign_up'}])
    ])
    if has_account['Login'] == 'login':
        username = login(users)

    elif has_account['Sign_Up'] == 'sign_up':
        sign_up(users)

    pywebio.session.info = {'username': username}
    pywebio.session.info['theme'] = users.search(Query().username == username)[0]['theme']


    while view_dashboard(users, username) == "reset":
        print("all systems operational")
    else:
        quit()

if __name__ == '__main__':
    start_server(app, port=8080, cdn=True)

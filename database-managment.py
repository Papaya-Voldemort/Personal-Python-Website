from tinydb import TinyDB, Query

users = TinyDB('users.json')

users.insert({'username': 'Eli', 'password': 'secret'})
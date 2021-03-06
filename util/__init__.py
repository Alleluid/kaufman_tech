from os import path
from flask_login import UserMixin

def get_key_from_file():
    try:
        with open(path.abspath("key"), 'rb') as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError("need `key` file with binary data.")

class User(UserMixin):
    pass

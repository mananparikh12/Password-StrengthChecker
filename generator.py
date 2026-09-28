import string
import secrets

def make_strong_password(length=14):
    all_chars = string.ascii_letters + string.digits + "!@#$%^&*"
    new_password = ""
    for i in range(length):
        new_password = new_password + secrets.choice(all_chars)
    return new_password

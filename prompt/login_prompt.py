from service.user_service import UserService
from getpass import getpass

def login_prompt(user_service:UserService):
    users = user_service.get_all_users()
    while True:
        username = input("Username: ")
        user = next((u for u in users if u.get_username() == username), None)
        if user != None:
            break
        print("Not a valid username. Try again.")
    while True:
        password = getpass("Password: ")
        if password == user.get_password():
            return user
        print("Incorrect password. Try again.")
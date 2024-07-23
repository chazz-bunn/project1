from service.user_service import UserService
from entity.user import User
from getpass import getpass

def create_account_prompt(user_service:UserService) -> User:
    users = user_service.get_all_users()
    usernames = [user.get_username() for user in users]
    username = ""
    password = ""
    while True:
        print("Enter your desired username")
        username = input("Username: ")
        if username not in usernames:
            break
        else:
            print("That username is already taken, please try again")
    while True:
        print("Enter a password. Password must be at least 6 characters long, contain at least one digit, and contain at least one special character")
        password = getpass("Password: ")
        if len(password) > 5:
            if any(char.isdigit() for char in password):
                if any(not char.isalnum() for char in password):
                    break
        print("Not an acceptable password. Try again.")
    return user_service.create_accout(username, password)
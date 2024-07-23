from service.user_service import UserService
from entity.user import User
from prompt.login_prompt import login_prompt
from prompt.create_account_prompt import create_account_prompt

def welcome_prompt(user_service:UserService) -> User:
    print("***********************************")
    print("Hello and Welcome to the Acme Store")
    print("***********************************")
    while True:
        print("[L]ogin if you're existing user, or")
        print("[C]reate a new account")
        option = input("Enter 'L' or 'C': ")
        if option.capitalize() == 'L':
            return login_prompt(user_service)
        elif option.capitalize() == 'C':
            return create_account_prompt(user_service)
        else:
            print("Enter 'L' or 'C'.")
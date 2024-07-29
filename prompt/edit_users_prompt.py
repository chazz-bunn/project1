from service.user_service import UserService
from entity.user import User
from prompt.make_table import make_table

def change_admin_privilege(user_service:UserService, users:list[User]):
    username = input("Enter username of user to grant admin privileges to: ")
    if username not in [u.get_username() for u in users]:
        print("That's not a username in the database. Try again.")
        input("Press Enter to continue: ")
    else:
        user = next(u for u in users if u.get_username() == username)
        user_service.grant_revoke_user_admin_privileges(user)
        user.set_admin_privileges(int(not user.get_admin_privileges()))
        table = make_table([[user.get_username(), user.get_password(), user.get_admin_privileges()]], ["Username", "Password", "Admin Privilege"])
        print("\n************\nUser Changed\n************")
        print(table)
        input("\nPress Enter to continue")

def remove_user(user_service:UserService, users:list[User]):
    username = input("Enter username of user to remove: ")
    if username not in [u.get_username() for u in users]:
        print("That's not a username in the database. Try again.")
        input("Press Enter to continue: ")
    else:
        user = next(u for u in users if u.get_username() == username)
        user_service.remove_user_by_username(user.get_username())
        table = make_table([[user.get_username(), user.get_password(), user.get_admin_privileges()]], ["Username", "Password", "Admin Privilege"])
        print("\n************\nUser Deleted\n************")
        print(table)
        input("\nPress Enter to continue")

def edit_users_prompt(user_service:UserService):
    while True:
        users = user_service.get_all_users()
        user_list = [[u.get_username(), u.get_password(), u.get_admin_privileges()] for u in users]
        table = make_table(user_list, ["Username", "Password", "Admin Privilege"])
        print("\n*****\nUsers\n*****")
        print(table)
        print("\n[1] Grant/Revoke User Admin Privilege\n[2] Remove User\n[3] Exit")
        option = input("Enter a number: ")
        if option == "1":
            change_admin_privilege(user_service, users)
        elif option == "2":
            remove_user(user_service, users)
        elif option == "3":
            break
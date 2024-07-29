from entity.user import User
from repository.user_repository import UserRepository

class UserService:
    def __init__(self):
        self.__user_repository = UserRepository()

    def create_accout(self, username, password) -> User:
        new_user = User(username, password, False)
        self.__user_repository.insert_user(new_user)
        return new_user
    
    def get_all_users(self) -> list[User]:
        return self.__user_repository.select_all_users()
    
    def grant_revoke_user_admin_privileges(self, user:User):
        print(user.get_username())
        if user.get_admin_privileges() == 1 or user.get_admin_privileges() == True:
            self.__user_repository.change_admin_privilege(user.get_username(), 0)
        else:
            self.__user_repository.change_admin_privilege(user.get_username(), 1)

    def remove_user_by_username(self, username:str):
        self.__user_repository.delete_user_with_username(username)
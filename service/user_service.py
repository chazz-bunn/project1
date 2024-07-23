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
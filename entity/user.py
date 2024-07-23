class User:
    def __init__(self, *args):
        self.__username = args[0]
        self.__password = args[1]
        self.__admin_privileges = args[2]
    
    def get_username(self) -> str:
        return self.__username
    def get_password(self) -> str:
        return self.__password
    def get_admin_privileges(self) -> bool:
        return self.__admin_privileges
    
    def set_username(self, new_username):
        self.__username = new_username
    def set_password(self, new_password):
        self.__password = new_password
    def set_admin_privileges(self, privilege):
        self.__admin_privileges = privilege
        
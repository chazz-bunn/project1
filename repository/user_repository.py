from connector import cnx
from connector import cursor
from entity.user import User

class UserRepository:
    def insert_user(self, user:User):
        cursor.execute("INSERT INTO users (username, password, admin_privileges) VALUES ('{}', '{}', {});".format(
            user.get_username().replace("'", "\\'"),
            user.get_password().replace("'", "\\'"),
            str(user.get_admin_privileges())
        ))
        cnx.commit()
    
    def select_all_users(self) -> list[User]:
        cursor.execute("SELECT * FROM users;")
        results = cursor.fetchall()
        return [User(*r) for r in results]
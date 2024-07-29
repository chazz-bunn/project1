from connector import cnx
from connector import cursor
from entity.user import User
import logging

class UserRepository:
    def insert_user(self, user:User):
        logging.info("Inserting into users table")
        cursor.execute("INSERT INTO users (username, password, admin_privileges) VALUES ('{}', '{}', {});".format(
            user.get_username().replace("'", "\\'"),
            user.get_password().replace("'", "\\'"),
            str(user.get_admin_privileges())
        ))
        cnx.commit()
    
    def select_all_users(self) -> list[User]:
        logging.info("Selecting all rows in users table")
        cursor.execute("SELECT * FROM users;")
        results = cursor.fetchall()
        return [User(*r) for r in results]
    
    def change_admin_privilege(self, username:str, privilege:str):
        logging.info("Changing user admin privileges")
        cursor.execute("UPDATE users SET admin_privileges = {} WHERE username = '{}';".format(
            privilege,
            username
        ))
        cnx.commit()

    def delete_user_with_username(self, username:str):
        logging.info("Deleting row from user table")
        cursor.execute("DELETE FROM users WHERE username = '{}';".format(username.replace("'", "\\'")))
        cnx.commit()
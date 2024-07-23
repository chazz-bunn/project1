from login_info.get_login_info import get_login_info
import mysql.connector

login = get_login_info()
cnx = mysql.connector.connect(user=login["user"], password=login["password"], host=login["host"], database=login["database"])
cursor = cnx.cursor()
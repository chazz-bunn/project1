from service.product_service import ProductService
from service.user_service import UserService
from service.order_service import OrderService

from connector import cnx
from connector import cursor

from prompt.welcome_prompt import welcome_prompt
from prompt.product_prompt import product_prompt
from prompt.personal_order_history_prompt import personal_order_history_prompt
from prompt.admin_control import admin_control

import logging

def main():
    logging.basicConfig(filename="myapp.log", level=logging.DEBUG, format='%(asctime)s :: %(message)s')

    product_service = ProductService()
    user_service = UserService()
    order_service = OrderService()

    user = welcome_prompt(user_service)
    while True:
        print("\nHello " + user.get_username() + ", what would you like to do?")
        print("[1] View Products\n[2] View Personal Order History\n""[3] Exit")
        if user.get_admin_privileges():
            print("[4] Admin Controls")

        option = input("Enter number: ")
        if option == "1":
            product_prompt(user, product_service, order_service)
        elif option == "2":
            personal_order_history_prompt(user, order_service, product_service)
        elif option == "3" and user.get_admin_privileges():
            break
        elif option == "4" and user.get_admin_privileges():
            admin_control(user_service, product_service, order_service)
        else:
            print("Invalid input. Try again.")
    
    cursor.close()
    cnx.close()
 
if __name__ == '__main__':
    main()
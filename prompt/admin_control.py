from service.product_service import ProductService
from service.user_service import UserService
from service.order_service import OrderService

from prompt.edit_products_prompt import edit_products_prompt
from prompt.edit_users_prompt import edit_users_prompt
from prompt.edit_orders_prompt import edit_orders_prompt

def admin_control(user_service:UserService, product_service:ProductService, order_service:OrderService):
    while True:
        print("\n**************\nAdmin Controls\n**************")
        print("What would you like to do?")
        print("[1] Update Products\n[2] View/Update Users\n[3] View/Update Order History\n[4] Exit admin controls")
        option = input("Enter a number: ")
        if option == '1':
            edit_products_prompt(product_service)
        elif option == '2':
            edit_users_prompt(user_service)
            pass
        elif option == '3':
            edit_orders_prompt(order_service)
            pass
        elif option == '4':
            break
        else:
            print("That's not an option. Try again.")
from entity.user import User
from service.product_service import ProductService
from service.order_service import OrderService
from prompt.make_table import make_table

def product_prompt(user:User, product_service:ProductService, order_service:OrderService):
    products = product_service.get_all_products()
    table = [[r.get_id(), r.get_name(), "$" + str(r.get_price()), r.get_description()] for r in products]
    pd_table = make_table(table, ["ID", "Name", "Price", "Description"])

    nother = ""
    while True:
        print("\n********\nProducts\n********")
        print(pd_table)
        print("\nWould you like to purchase a{} product?".format(nother))
        option = input("y/n: ")
        if option.lower() == 'n':
            break
        if option.lower() == 'y':
            print("Enter the ID number of the product you would like to purchase: ", end = '')
            while True:
                id = input()
                if int(id) not in [r.get_id() for r in products]:
                    print("That's not a product id. Try again.")
                else:
                    price = next(p.get_price() for p in products if p.get_id() == int(id))
                    order_service.add_order(int(id), user.get_username(), price)
                    break
            nother = "nother"
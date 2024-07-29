from service.order_service import OrderService
from prompt.make_table import make_table

def edit_orders_prompt(order_service:OrderService):
    while True:
        orders = order_service.get_all_orders()
        orders_list = [[o.get_id(), 
                        o.get_date_orderd(), 
                        o.get_product_id(), 
                        order_service.get_product_name_with_product_id(o.get_product_id()),
                        o.get_username(),
                        "$" + str(o.get_price_paid())] 
                        for o in orders]
        table = make_table(orders_list, ["ID", "Date Ordered", "Product ID", "Product Name", "Username", "Paid"])
        print("\n******\nOrders\n******")
        print(table)
        print("\nDo you want to remove an order?")
        option = input("y/n: ")
        if option == 'y':
            id = input("Enter ID of order you want removed: ")
            if int(id) not in [o.get_id() for o in orders]:
                print("That's not an ID of an order. Try again.")
            else:
                order = next(o for o in orders if o.get_id() == int(id))
                order_service.remove_order_with_id(int(id))
                table = make_table([[
                    order.get_id(), 
                    order.get_date_orderd(), 
                    order.get_product_id(), 
                    order_service.get_product_name_with_product_id(order.get_product_id()),
                    order.get_username(),
                    "$" + str(order.get_price_paid())]],
                    ["ID", "Date Ordered", "Product ID", "Product Name", "Username", "Paid"]
                )
                print("\n*************\nOrder Deleted\n*************")
                print(table)
                input("\nPress Enter to continue")
        elif option == 'n':
            break
        else:
            print("Invalid input. Input 'y' or 'n'.")
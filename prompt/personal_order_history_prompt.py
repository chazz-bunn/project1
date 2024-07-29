from entity.user import User
from service.order_service import OrderService
from service.product_service import ProductService
from prompt.make_table import make_table

def personal_order_history_prompt(user:User, order_servie:OrderService, product_service:ProductService):
    orders = order_servie.get_orders_by_username(user.get_username())
    table = [[o.get_date_orderd(), product_service.get_product_name_by_id(o.get_product_id()), "$" + str(o.get_price_paid())] for o in orders]
    pd_table = make_table(table, ["Date Ordered", "Product", "Paid"])
    print("\n*********************\n{}'s Order History\n*********************".format(user.get_username()))
    print(pd_table)
    input("\nPress Enter to continue")
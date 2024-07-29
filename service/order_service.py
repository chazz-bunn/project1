from repository.order_repository import OrderRepository
from entity.order import Order

class OrderService:
    def __init__(self):
        self.__order_repository = OrderRepository()

    def add_order(self, product_id:int, username:str, price_paid:float) -> Order:
        id, date_ordered = self.__order_repository.insert_order(product_id, username, price_paid)
        return Order(id, date_ordered, product_id, username, price_paid)

    def get_orders_by_username(self, username:str) -> list[Order]:
        name = self.__order_repository.select_orders_by_username(username)
        return name
    
    def get_all_orders(self) -> list[Order]:
        return self.__order_repository.select_all_orders()
    
    def get_product_name_with_product_id(self, product_id):
        return self.__order_repository.select_product_name_with_product_id(product_id)
    
    def remove_order_with_id(self, id):
        self.__order_repository.delete_order_with_id(id)
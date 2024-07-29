from entity.product import Product
from repository.product_repository import ProductRepository

class ProductService:
    def __init__(self):
        self.__product_repository = ProductRepository()

    def add_product(self, name, price, description):
        new_product = Product(name, price, description)
        id = self.__product_repository.insert_product(new_product)
        new_product.set_id(id)
        return new_product

    def get_all_products(self) -> list[Product]:
        return self.__product_repository.select_all_products()
    
    def get_product_name_by_id(self, id:int) -> str:
        return self.__product_repository.select_product_name_with_id(id)
    
    def delete_product_by_id(self, id:int):
        self.__product_repository.delete_product_with_id(id)

    def change_product_name_by_id(self, id:int, new_name:str):
        self.__product_repository.update_product_name_with_id(id, new_name)

    def change_product_price_by_id(self, id:int, new_price:float):
        self.__product_repository.update_product_price_with_id(id, new_price)

    def change_product_description_by_id(self, id:int, new_description:str):
        self.__product_repository.update_product_description_with_id(id, new_description)
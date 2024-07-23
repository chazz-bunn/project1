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

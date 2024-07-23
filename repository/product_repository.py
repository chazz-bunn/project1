from connector import cnx
from connector import cursor
from entity.product import Product

class ProductRepository:
    def insert_product(self, product:Product) -> int:
        cursor.execute("INSERT INTO products (name, price, description) VALUES ('{}', {}, '{}')".format(
            product.get_name().replace("'", "\\'"), 
            product.get_price(), 
            product.get_description().replace("'", "\\'")
        ))
        cnx.commit()
        return cursor.lastrowid


from connector import cnx
from connector import cursor
from entity.product import Product
import logging

class ProductRepository:
    def insert_product(self, product:Product) -> int:
        logging.info("Inserting product into table")
        cursor.execute("INSERT INTO products (name, price, description) VALUES ('{}', {}, '{}');".format(
            product.get_name().replace("'", "\\'"), 
            product.get_price(), 
            product.get_description().replace("'", "\\'")
        ))
        cnx.commit()
        return cursor.lastrowid

    def select_all_products(self) -> list[Product]:
        logging.info("Selecting all rows in products table")
        cursor.execute("SELECT * FROM products;")
        results = cursor.fetchall()
        return [Product(*r) for r in results]
    
    def select_product_name_with_id(self, id:int):
        logging.info("Selecting name from products table with id")
        cursor.execute("SELECT name FROM products WHERE id = {};".format(id))
        result = cursor.fetchone()
        return result[0]
    
    def delete_product_with_id(self, id:int):
        logging.info("Deleting name from products table with id")
        cursor.execute("DELETE FROM products WHERE id = {};".format(id))
        cnx.commit()

    def update_product_name_with_id(self, id:int, new_name:str):
        logging.info("Updating name in products table with id")
        cursor.execute("UPDATE products SET name = '{}' WHERE id = {};".format(new_name.replace("'", "\\'"), id))
        cnx.commit()

    def update_product_price_with_id(self, id:int, new_price:float):
        logging.info("Updating product price in products table with id")
        cursor.execute("UPDATE products SET price = {} WHERE id = {};".format(new_price, id))
        cnx.commit()
    
    def update_product_description_with_id(self, id:int, new_description:str):
        logging.info("Updating description in products table with id")
        cursor.execute("UPDATE products SET description = '{}' WHERE id = {};".format(new_description.replace("'", "\\'"), id))
        cnx.commit()
from connector import cnx
from connector import cursor
from entity.order import Order
import datetime
import logging

class OrderRepository:
    def insert_order(self, product_id:int, username:str, price_paid:float) -> list[int, datetime.datetime]:
        logging.info("Inserting into orders table")
        date_ordered = datetime.datetime.now()
        date_ordered = (date_ordered + datetime.timedelta(milliseconds=500)).replace(microsecond=0)
        cursor.execute(
            "INSERT INTO orders (date_ordered, product_id, username, price_paid) VALUES ('{}', {}, '{}', {})".format(
                date_ordered,
                product_id,
                username.replace("'", "\\'"),
                price_paid
            )
        )
        cnx.commit()
        return [cursor.lastrowid, date_ordered]
    
    def select_all_orders(self):
        logging.info("Select all rows in orders table")
        cursor.execute("SELECT * FROM orders;")
        results = cursor.fetchall()
        return [Order(*r) for r in results]

    def select_orders_by_username(self, username:str):
        logging.info("Select all rows in orders table with username")
        cursor.execute("SELECT * FROM orders WHERE username = '{}';".format(username))
        results = cursor.fetchall()
        return [Order(*r) for r in results]
    
    def select_product_name_with_product_id(self, product_id):
        logging.info("Select row in products table with id")
        cursor.execute("SELECT name FROM products WHERE id = {};".format(product_id))
        result = cursor.fetchone()
        return result[0]
    
    def delete_order_with_id(self, id):
        logging.info("Delete row in orders table with id")
        cursor.execute("DELETE FROM orders WHERE id = {};".format(id))
        cnx.commit()
class Order:
    def __init__(self, *args):
        if len(args) == 5:
            self.__id = args[0]
            self.__date_ordered = args[1]
            self.__product_id = args[2]
            self.__username = args[3]
            self.__price_paid = args[4]
        elif len(args) == 4:
            self.__date_ordered = args[0]
            self.__product_id = args[1]
            self.__username = args[2]
            self.__price_paid = args[3]
    
    def get_id(self):
        return self.__id
    def get_date_orderd(self):
        return self.__date_ordered
    def get_product_id(self):
        return self.__product_id
    def get_username(self):
        return self.__username
    def get_price_paid(self):
        return self.__price_paid

    def set_id(self, id):
        self.__id = id
    def set_date_ordered(self, date_ordered):
        self.__date_ordered = date_ordered
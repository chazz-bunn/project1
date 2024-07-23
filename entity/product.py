class Product:
    def __init__(self, *args):
        if isinstance(args[0], int):
            self.__id = args[0]
            self.__name = args[1]
            self.__price = args[2]
            self.__description = args[3]
        else:
            self.__id = None
            self.__name = args[0]
            self.__price = args[1]
            self.__description = args[2]
    
    def get_id(self) -> int:
        return self.__id
    def get_name(self) -> str:
        return self.__name
    def get_price(self) -> float:
        return self.__price
    def get_description(self) -> str:
        return self.__description
    
    def set_id(self, id):
        self.__id = id
    def set_name(self, new_name):
        self.__name = new_name
    def set_price(self, new_price):
        self.__price = new_price
    def set_description(self, new_description):
        self.__description = new_description
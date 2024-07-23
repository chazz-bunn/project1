from service.product_service import ProductService
from service.user_service import UserService
from connector import cnx
from connector import cursor
import logging
from prompt.welcome_prompt import welcome_prompt

logger = logging.getLogger(__name__)

def main():
    logging.basicConfig(filename='myapp.log', level=logging.INFO)

    logger.info('Start: Creating service objects')
    product_service = ProductService()
    user_service = UserService()
    logger.info('End: Creating service objects')
    
    #welcome_prompt(user_service)
    """ while True:
        print("\nHello " + user.get_username() + ", what would you like to do?")
        print("[1] View Inventory\n[2] View Personal Order History")
        if user.get_admin_privileges():
            print("[3] Admin Controls")
            break """

    
    cursor.close()
    cnx.close()
 
if __name__ == '__main__':
    main()
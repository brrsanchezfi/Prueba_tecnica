from modules.view.views import menu
from database.database_manager import create_tables

if __name__ == '__main__':
    
    create_tables()
    menu()
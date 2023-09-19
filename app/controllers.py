from app.model import Product

import sqlite3
import os

db_path = os.path.join("database", "inventory.db")


def show_product_controller():

    """Retorna todos los productos registrados hasta el momento

    Returns:
        _type_: list[tuples[]]
    """

    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Products")
            products = cursor.fetchall()
            return products
    
    
    except sqlite3.Error as e:
        print("Error al obtener todos los productos:", str(e))
        return None
    


def create_product_controller( code:str , name:str , quantity:int , state:bool=False, id:int=None ):

    """Funcion para crear producto
    """

    producto = Product( id , code , name , quantity , state)

    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO Products (name,code,quantity,state) 
                        VALUES (?,?,?,?)''', (producto.name, producto.code , producto.quantity , producto.state))
            conn.commit()
    except sqlite3.Error as e:
        print("Error al registrar el producto:", str(e))


    
def withdraw_product_controller( code:str , withdrawal_quantity:int ):

    """funcion que
            1. verifica la cantidad disponible
            2. verificado la cantidad procede a actualizar la nueva cantidad

    Args:
        code (str): codigo de producto 
        withdrawal_quantity (int): cantidad que queremos retirar
    """

    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''SELECT quantity FROM Products WHERE code = ?''', (code,))
            current_quantity = cursor.fetchone()[0]

            if current_quantity >= withdrawal_quantity:
                # Realizar el retiro
                cursor.execute('''UPDATE Products SET quantity = quantity - ? WHERE code = ?''', (withdrawal_quantity, code))
                conn.commit()
                print(f"Se retiraron {withdrawal_quantity} unidades del producto {code}.")
            else:
                print(f"No hay suficiente cantidad de producto {code} para retirar.")
    except sqlite3.Error as e:
        print("Error al retirar el producto:", str(e))



def update_product_state_controller( code:str , new_state:bool , withdrawal_quantity:int ):
    """Sirve para registrar los defectuodos, ademas desencadena untrigger que registra el evento en
        otra tabla

    Args:
        code (str): _description_
        new_state (bool): _description_
        withdrawal_quantity (int): _description_
    """

    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''SELECT quantity FROM Products WHERE code = ?''', (code,))
            current_quantity = cursor.fetchone()[0]
            cursor.execute('''SELECT state FROM Products WHERE code = ?''', (code,))
            current_state = cursor.fetchone()[0]

            if current_quantity >= withdrawal_quantity:
                # Realizar el retiro
                cursor.execute('''UPDATE Products SET quantity = quantity - ?, state = ? WHERE code = ?''', (withdrawal_quantity, not current_state, code))
                conn.commit()
                print(f"Se retiraron {withdrawal_quantity} unidades del producto {code}.")
            else:
                print(f"No hay suficiente cantidad de producto {code} para retirar.")

    except sqlite3.Error as e:
        print("Error al actualizar el estado del producto:", str(e))



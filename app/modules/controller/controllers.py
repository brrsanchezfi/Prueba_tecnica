from ..model.model import Product
import csv
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
            cursor.execute("SELECT code, name, quantity FROM Products")
            products = cursor.fetchall()
            return products
    
    
    except sqlite3.Error as e:
        print("Error al obtener todos los productos:", str(e))
        return None
    
def show_withdraw():

    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT code, name, quantity, date FROM Withdraw")
            products = cursor.fetchall()
            return products
    
    
    except sqlite3.Error as e:
        print("Error al obtener todos los productos:", str(e))
        return None

def show_defective():
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT code, name, quantity, date FROM Defective")
            products = cursor.fetchall()
            return products
    
    
    except sqlite3.Error as e:
        print("Error al obtener todos los productos:", str(e))
        return None

def create_product_controller( code:str , name:str , quantity:int , state:bool=False, id:int=None ):

    """Funcion para crear producto
    """

    producto = Product( id , code , name , quantity , 0)

    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()

            cursor.execute('''SELECT id, quantity FROM Products WHERE code = ?''', (code,))
            existing_product = cursor.fetchone()

            if existing_product:
                # Si el producto existe, actualiza la cantidad sumándola
                product_id, existing_quantity = existing_product
                new_quantity = existing_quantity + quantity
                cursor.execute('''UPDATE Products SET quantity = ? WHERE code = ?''', (producto.quantity, producto.code))
            else:
                # Si el producto no existe, crea uno nuevo
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

def withdraw_products_controller(archivo_csv):


    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        # Leer el archivo CSV y actualizar la base de datos
        with open(archivo_csv, 'r', newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)  # Saltar la fila de encabezados si la tiene

            for row in csvreader:
                        code, name, quantity = row[0], row[1] , int(row[2])
                        print(row[0], row[1] , int(row[2]))
                        # Verificar si el producto ya existe en la base de datos
                        cursor.execute("SELECT code, quantity FROM Products WHERE code =?", (code,))
                        resultado = cursor.fetchone()

                        if resultado:
                            # Si el producto existe, actualiza la cantidad
                            producto_id, cantidad_existente = resultado
                            nueva_cantidad = cantidad_existente + quantity
                            cursor.execute("UPDATE Products SET quantity=? WHERE code=?", (nueva_cantidad, code))
                        else:
                            # Si el producto no existe, agrégalo a la base de datos
                            cursor.execute("INSERT INTO Products (code, name, quantity, state) VALUES (?, ?, ?, ?)", (code, name, quantity, 0))

                # Guardar los cambios en la base de datos y cerrar la conexión


def update_product_state_controller( code:str , withdrawal_quantity:int ):
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

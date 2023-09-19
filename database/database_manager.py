
import sqlite3
import os

db_path = os.path.join("database", "inventory.db")


def create_tables():
    """Crea la base de datos, primero comprueba que no existe
        y crea el trigger para actualizar quantity
    """
    try:
        with sqlite3.connect(db_path) as conn:
            cursor=conn.cursor()

            cursor.execute('''CREATE TABLE IF NOT EXISTS Products(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            code VARCHAR(10) UNIQUE ,
                            name VARCHAR(50),
                            quantity INTEGER, 
                            state BOOLEAN DEFAULT 0  -- comodin
                            )''')
            
            cursor.execute('''CREATE TABLE IF NOT EXISTS Withdraw(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            code VARCHAR(10),
                            name VARCHAR(50),
                            quantity INTEGER,
                            state BOOLEAN DEFAULT 0,
                            date TEXT,
                            FOREIGN KEY (code) REFERENCES Products (code)
                            )''')
            
            cursor.execute('''CREATE TABLE IF NOT EXISTS Defective( 
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                            code VARCHAR(10),
                            name VARCHAR(50),
                            quantity INTEGER,
                            state BOOLEAN DEFAULT 0,
                            date TEXT,
                            FOREIGN KEY (code) REFERENCES Products (code),
                            FOREIGN KEY (code) REFERENCES  Withdraw (code)
                            )''')
            
            # Trigger para registrar eventos en Withdraw cuando se actualiza Products
            cursor.execute('''CREATE TRIGGER IF NOT EXISTS products_to_withdraw_trigger
                            AFTER UPDATE OF quantity ON Products
                            FOR EACH ROW
                            BEGIN
                                INSERT INTO Withdraw (code, name, quantity, state, date)
                                VALUES (NEW.code, NEW.name, NEW.quantity, NEW.state, DATETIME('now'));
                            END;''')

            # Trigger para registrar eventos en Defective cuando se actualiza Products
            cursor.execute('''CREATE TRIGGER IF NOT EXISTS products_to_defective_trigger
                            AFTER UPDATE OF quantity, state ON Products
                            FOR EACH ROW
                            BEGIN
                                INSERT INTO Defective (code, name, quantity, state, date)
                                VALUES (NEW.code, NEW.name, NEW.quantity, 1 , DATETIME('now'));
                            END;''')

    except sqlite3.Error as e:
        print("Funtion - create_tables -- || -- " , str(e))

create_tables()
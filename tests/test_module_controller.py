import sys
import os
import sqlite3
import unittest
from io import StringIO
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.modules.controller.controllers import *


class TestProductController(unittest.TestCase):

    def setUp(self):
        # Prepara una base de datos de prueba en memoria
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_test_tables()

    def tearDown(self):
        # Cierra la conexión a la base de datos de prueba
        self.conn.close()

    def create_test_tables(self):
        # Crea tablas de prueba en la base de datos de memoria
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Products(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            code VARCHAR(10) UNIQUE,
                            name VARCHAR(50),
                            quantity INTEGER,
                            state BOOLEAN DEFAULT 0
                            )''')

    def test_create_product_controller(self):
        # Prueba la función create_product_controller
        create_product_controller("P001", "Producto de prueba", 10, False, None)
        self.cursor.execute("SELECT * FROM Products WHERE code=?", ("P001",))
        product = self.cursor.fetchone()
        self.assertIsNotNone(product)
        self.assertEqual(product[1], "P001")
        self.assertEqual(product[2], "Producto de prueba")
        self.assertEqual(product[3], 10)
        self.assertEqual(product[4], 0)

    def test_withdraw_product_controller(self):
        # Prueba la función withdraw_product_controller
        create_product_controller("P002", "Producto de prueba 2", 20, False, None)
        withdraw_product_controller("P002", 5)
        product = self.cursor.execute("SELECT * FROM Products WHERE code=?", ("P002",)).fetchone()
        self.assertIsNotNone(product)
        self.assertEqual(product[1], "P002")
        self.assertEqual(product[2], "Producto de prueba 2")
        self.assertEqual(product[3], 15)

    def test_update_product_state_controller(self):
        # Prueba la función update_product_state_controller
        create_product_controller("P003", "Producto de prueba 3", 30, False, None)
        update_product_state_controller("P003", 10)
        product = self.cursor.execute("SELECT * FROM Products WHERE code=?", ("P003",)).fetchone()
        self.assertIsNotNone(product)
        self.assertEqual(product[1], "P003")
        self.assertEqual(product[2], "Producto de prueba 3")
        self.assertEqual(product[4], 1)  # El estado debería ser 1 (defectuoso) después de la actualización


    def test_withdraw_products_controller(self):
        # Prueba la función withdraw_products_controller

        # Simula un archivo CSV como una cadena (puedes ajustar los datos según tus necesidades)
        csv_data = StringIO("""Code,Name,Quantity,state
                             P001,Producto 1,5,1
                             P002,Producto 2,10,1
                             P003,Producto 3,15,1
                             """)

        # Llama a la función para procesar el archivo CSV simulado
        withdraw_products_controller(csv_data)

        # Verifica si los productos se han actualizado correctamente en la base de datos
        product_1 = self.cursor.execute("SELECT * FROM Products WHERE code=?", ("P004",)).fetchone()
        product_2 = self.cursor.execute("SELECT * FROM Products WHERE code=?", ("P005",)).fetchone()
        product_3 = self.cursor.execute("SELECT * FROM Products WHERE code=?", ("P006",)).fetchone()

        self.assertIsNotNone(product_1)
        self.assertIsNotNone(product_2)
        self.assertIsNotNone(product_3)

        self.assertEqual(product_1[1], "P004")
        self.assertEqual(product_1[2], "Producto 4")
        self.assertEqual(product_1[3], 5)

        self.assertEqual(product_2[1], "P005")
        self.assertEqual(product_2[2], "Producto 5")
        self.assertEqual(product_2[3], 10)

        self.assertEqual(product_3[1], "P006")
        self.assertEqual(product_3[2], "Producto 6")
        self.assertEqual(product_3[3], 15)

if __name__ == "__main__":
    unittest.main()


import sqlite3
from controllers import *
# Importa las funciones y clases que deseas probar desde tu módulo o archivo principal



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

    # Agrega más métodos de prueba para las otras funciones

if __name__ == "__main__":
    unittest.main()

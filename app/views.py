from controllers import create_product_controller,show_product_controller 
from tabulate import tabulate

import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def submenu_1():
    clear()
    print('''
            Productos Registrados

             ''')

    print(tabulate(show_product_controller(),headers=["Codigo" , "Nombre del Producto" , "Cantidad" , "Estado"]))
    input()

def submenu_2():
    while(True):
        clear()
        print('''
              
            Ingrese los datos del producto
              
              ''')

        code = input("Ingrese codigo de producto")
        name = input("Ingrese nombre del producto")
        state = input('''estado del producto, por defecto es no defectuoso
                        1. defectuoso''')
        if state == '1': state = True
        if state != '1': state = False
        else: continue
        
        quantity = input("Por favor, ingresa la cantidad del producto: ")

        try:
            quantity = int(quantity)
        except ValueError:
            print("La entrada no es un número entero válido.")

        create_product_controller(code=code, name=name, state=state, quantity=quantity)

        input("Enter para regresar al menu principal")
        break
 
def submenu_3():
    clear()
    print('''
            Sistema gestor de carga de archivos para la ingesta masiva de inventario
          
                acontinuacion siga las instrucciones, asegurese de que sua archivo 
                dentro de un localPath 

                1. prepare un archivo .csv, .xml, .json que contenga 4 columnas o atributos
                        ++--------+--------------------+----------+--------------++
                        || Codigo | Nombre de Producto | Cantidad | Estado (1/0) ||
                        ++--------+--------------------+----------+--------------++    
                2. pegue la ruta del su archivo:
                    Ejemplo : c://
        ''')
    p=input()

def submenu_4():
    clear()
    p=print('''
          
            Registro de salida de productos
    ''')
    p=input()

def submenu_5():
    clear()
    print('''
          
            Registro de productos defectuosos
    ''')
    p=input()

def menu():
    create_tables()
    clear() 
    while(True):
        clear()
        print('''
              
              Bienvenidos al sistema de Registro de enventario
                    
                    1. Visualizar Productos en Stock
                    2. Registrar Producto Nuevo al Stock (Individual)
                    3. Registrar Producto Nuevo al Stock (Masivo)
                    4. Registar Salida del Producto
                    5. Marcar Producto como Defectuoso
              
                    6. Salir
              
        ''')

        selection = input("seleccione el item con el que desea interactuar y presione : ")

        if selection == '1': submenu_1()

        if selection == '2': submenu_2()

        if selection == '3': submenu_3()

        if selection == '4': print("show")
        if selection == '5': print("show")
        if selection == '6': break
        else: continue 


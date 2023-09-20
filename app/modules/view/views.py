from ..controller.controllers import *
from tabulate import tabulate

import tkinter as tk
from tkinter import filedialog

import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('''
              

  ####    ##   ##  ##   ##  #######  ##   ##  ######     ##     ######    ####     #####
   ##     ###  ##   ##  ##   #  ###  ##  ###    ##      ####     ##  ##    ##     ##   ##
   ##     #### ##   ## ##    ## #    #### ##    ##     ##  ##    ##  ##    ##     ##   ##
   ##     ## ####   ## ##    ####    ## ####    ##     ##  ##    #####     ##     ##   ##
   ##     ##  ###    ###     ## #    ##  ###    ##     ######    ## ##     ##     ##   ##
   ##     ##   ##    ###     ##   #  ##   ##    ##     ##  ##    ##  ##    ##     ##   ##
  ####    ##   ##     #     #######  ##   ##   ####    ##  ##   #### ##   ####     #####

                            Sistema de Registro            
              ''')

def show_all_time():
    clear()
    print('''
                        Productos Registrados

             ''')

    print(tabulate(show_product_controller(),headers=["Codigo" , "Nombre del Producto" , "Cantidad" ]))

def submenu_1():

    while(True):
        clear()
        print('''
                Productos Registrados

                    1. Inventario
                    2. Historial de retiros
                    3. Historial Productos defectuosos

                ''')
        selection_submenu_1=input('Ingerse opcion: ')

        if selection_submenu_1=='1' :  
            print(tabulate(show_product_controller(),headers=["Codigo" , "Nombre del Producto" , "Cantidad" ]))
            input('presione ENTER para Regresar: ')
            break
        if selection_submenu_1=='2' :  
            print(tabulate(show_withdraw(),headers=["Codigo" , "Nombre del Producto" , "Cantidad" , "date"]))
            input('presione ENTER para Regresar: ')
            break
        if selection_submenu_1=='3' :  
            print(tabulate(show_defective(),headers=["Codigo" , "Nombre del Producto" , "Cantidad" , "date"]))
            input('presione ENTER para Regresar: ')
            break

def submenu_2():
    while(True):
        clear()
        show_all_time()

        print('''
        ------------------------------------------------------------------------------
        ''')


        code = input("Ingrese codigo de producto: ")
        name = input("Ingrese nombre del producto: ")
        quantity = None  # Inicializamos quantity como None

        error_occurred = False  # Variable para rastrear si ocurrió un error

        while quantity is None:
            try:
                quantity = int(input("Por favor, ingresa la cantidad del producto: "))
            except ValueError:
                error_occurred = True  # Marcamos que ocurrió un error
                clear()  # Borramos la pantalla antes de mostrar el mensaje de error
                print("La entrada no es un número entero válido.")

        if not error_occurred:
            create_product_controller(code=code, name=name, state=0, quantity=quantity)

        input("Enter para regresar al menu principal...")
        break
 
def submenu_3():
    clear()

    def abrir_dialogo_seleccion_archivo():
        archivo_csv = filedialog.askopenfilename(filetypes=[("Archivos CSV", "*.csv")])
        archivo_csv = os.path.normpath(archivo_csv)

        if archivo_csv:
            withdraw_products_controller(archivo_csv)
            ventana.destroy()

    print('''
            Sistema gestor de carga de archivos para la ingesta masiva de inventario
          
                acontinuacion siga las instrucciones, asegurese de que sua archivo 
                dentro de un localPath 

                1. prepare un archivo .csv, que contenga 3 columnas o atributos
                        ++--------+--------------------+----------++
                        || Codigo | Nombre de Producto | Cantidad ||
                        ++--------+--------------------+----------++    
                2. Se abrira un explorador de archivos para encontrar la hubicacion 
                    del archivo, seleccionelo y cierre la centana para continuar
        ''')

    # Crear una ventana de tkinter
    ventana = tk.Tk()
    ventana.title("Seleccionar archivo CSV")

    # Crear un botón para abrir el diálogo de selección de archivos
    boton_seleccion = tk.Button(ventana, text="Seleccionar archivo CSV", command=abrir_dialogo_seleccion_archivo)
    boton_seleccion.pack(padx=100, pady=50)

    # Ejecutar la ventana principal de tkinter
    ventana.mainloop()
    input("Presione ENTER para continuar...")

def submenu_4():
    clear()
    show_all_time()
    print('''
          
            Registro de salida de productos
    ''')
    code=input('Ingrese el codigo del producto: ')

    while(True):
        quantity=int(input('Ingrese la cantidad de producto que desea retirar: '))
        if type(quantity)==int: break

    withdraw_product_controller(code,quantity)

    input('Producto retirado y marcado como defectuoso, presione ENTER para continuar: ')

def submenu_5():
    clear()
    print('''
          
            Registro de productos defectuosos
    ''')
    code=input('Ingrese el codigo del producto defectuoso: ')

    while(True):
        quantity=int(input('Ingrese la cantidad: '))
        if type(quantity)==int: break

    update_product_state_controller( code , quantity )

    input('Producto retirado y marcado como defectuoso, presione ENTER para continuar: ')
    
def menu():
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
        if selection == '4': submenu_4()
        if selection == '5': submenu_5()
        if selection == '6': break
        else: continue 
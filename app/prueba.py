import os

def clear_bottom():
    # Borra solo las últimas 10 líneas de la pantalla
    os.system('cls' if os.name == 'nt' else 'clear')
    print('''
    ##     ##   ##  ##   ##  #######  ##   ##  ######     ##     ######    ####     #####
          ###  ##  ##   ##   ##   #  ###  ##  # ## #    ####     ##  ##    ##     ##   ##
  ###     #### ##   ## ##    ## #    #### ##    ##     ##  ##    ##  ##    ##     ##   ##
   ##     ## ####   ## ##    ####    ## ####    ##     ##  ##    #####     ##     ##   ##
   ##     ##  ###    ###     ## #    ##  ###    ##     ######    ## ##     ##     ##   ##
   ##     ##   ##    ###     ##   #  ##   ##    ##     ##  ##    ##  ##    ##     ##   ##
  ####    ##   ##     #     #######  ##   ##   ####    ##  ##   #### ##   ####     #####

    Ingrese los datos del producto
    ''')

def submenu_2():
    while True:
        clear_bottom()

        code = input("Ingrese codigo de producto: ")
        name = input("Ingrese nombre del producto: ")
        quantity = None  # Inicializamos quantity como None

        error_occurred = False  # Variable para rastrear si ocurrió un error

        while quantity is None:
            try:
                quantity = int(input("Por favor, ingresa la cantidad del producto: "))
            except ValueError:
                error_occurred = True  # Marcamos que ocurrió un error
                clear_bottom()  # Borramos la pantalla antes de mostrar el mensaje de error
                print("La entrada no es un número entero válido.")

        if not error_occurred:
            print('hola mundo')

        input("Enter para regresar al menu principal")
        break

submenu_2()

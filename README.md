

# Prueba Técnica: Gestión de Inventario en Python con SQLite

Este proyecto es una prueba técnica que implementa una solución en Python para la gestión de inventario de una bodega. La solución utiliza una arquitectura MVC (Modelo-Vista-Controlador) y se incluyen pruebas unitarias para el controlador.

## Requisitos Previos

Asegúrate de tener Python 3.x instalado en tu sistema. Puedes descargarlo desde el sitio web oficial de Python: [python.org](https://www.python.org/downloads/).

## Configuración del Entorno

1. Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/brrsanchezfi/Prueba_tecnica.git
```

2. Navega al directorio del proyecto:

```bash
cd inventario-bodega
```

3. Crea un entorno virtual para este proyecto (opcional pero recomendado):

```bash
python -m venv venv
```

4. Activa el entorno virtual:

En Windows:

```bash
venv\Scripts\activate
```

En macOS y Linux:

```bash
source venv/bin/activate
```

5. Instala las dependencias del proyecto:

```bash
pip install -r requirements.txt
```

## Estructura del Proyecto

El proyecto sigue una estructura MVC básica configurada en modulos:

- `model.py`: Define la estructura de datos y la lógica del modelo.
- `view.py`: Maneja la interfaz de usuario y la presentación de datos.
- `controller.py`: Controla la lógica de negocio y actúa como intermediario entre el modelo y la vista yu la base de datos.
- `database_manager.py`: Configura la base de datos SQLite.

## Uso del Programa

1. Ejecuta la aplicación:

```bash
python main.py
```

2. Utiliza la interfaz de usuario para agregar, actualizar o eliminar productos en el inventario.

## Pruebas Unitarias

Se han incluido pruebas unitarias para el controlador en el archivo `test_controller.py`. Puedes ejecutar estas pruebas con el siguiente comando:

```bash
python -m unittest test_module_controller.py
```


## Licencia

Este proyecto se encuentra bajo la licencia [none](LICENSE).

## Contacto

Si tienes alguna pregunta o comentario, no dudes en contactarme en [brrsanchezfi@gmail.com](mailto:tu@email.com).

---





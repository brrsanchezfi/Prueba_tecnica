class Product:

    def __init__(self, id:int, code:str, name:str, quantity:int, state:bool = False) -> None:

        """Constructor

        Args:
            id (int): autoincremental
            code(str): codigo o etiqueta de producto ( ejemplo = <A-1> )
            name (str): nombre del producto
            quantity (int): cantidad de producto
            state (bool): estado del pruducto (False default)

        """
        
        self.id = id
        self.code = code
        self.name = name
        self.state = state
        self.quantity = quantity
        

    def __str__(self):
        """To_string

        Returns:
            _type_: str
        """
        return f"ID: {self.id}, Nombre: {self.name}, Código: {self.code}, Estado: {self.state}, Cantidad: {self.quantity}"
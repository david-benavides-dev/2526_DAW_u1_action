
def saludo(nombre: str) -> str:
    """
    Recibe una palabra por parámetro y retorna un string concatenando la misma junto a un hola" ex-> "Hola, David!"
    Args:
        nombre(str): Nombre o palabra a saludar.

    Returns:
        str: Una cadena con el saludo personalizado de "Hola" + la palabra recibida por parámetro.
    """
    return f"Hola, {nombre}!"
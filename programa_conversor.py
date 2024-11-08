import pandas as pd


# Definimos la función para convertir de centímetros a pulgadas
def cm_a_pulgadas(cm):
    """
    Convierte una medida en centímetros a pulgadas.

    Args:
        cm (float): La longitud en centímetros a convertir.

    Returns:
        float: La longitud convertida en pulgadas.

    Ejemplo:
        >>> cm_a_pulgadas(2.54)
        1.0
    """
    return cm / 2.54


# Leemos el archivo Excel que contiene los datos de medidas en centímetros
df = pd.read_excel("muebles_medidas.xlsx")

# Añadimos una nueva columna al DataFrame 'df' que convierte las medidas de centímetros a pulgadas
df["Pulgadas"] = df["Centímetros"].apply(cm_a_pulgadas)

# Guardamos el DataFrame actualizado en un nuevo archivo Excel
df.to_excel("muebles_medidas_convertidas.xlsx", index=False)

# Mensaje para indicar que la conversión se ha completado y el archivo ha sido guardado
print(
    "Conversión completada. El archivo ha sido guardado como 'muebles_medidas_convertidas.xlsx' con las medidas en pulgadas."
)

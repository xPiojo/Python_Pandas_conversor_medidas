import pandas as pd

# Dataframe es la informacion basica con las piezas y centimetros para poder armar el Exel

data = {
    "Piezas:": ["Pata", "Tablero", "Puerta", "Estante", "Panel Lateral"],
    "Centímetros": [40, 120, 60, 30, 180],
}

df = pd.DataFrame(data)

# Guardar el Dataframe en un archivo Excel
df.to_excel("muebles_medidas.xlsx", index=False)

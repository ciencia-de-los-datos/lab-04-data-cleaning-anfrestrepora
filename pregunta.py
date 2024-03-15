"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data(df):

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0) # El index_col=0 permite que no se genere una columna adicional en el df xD
        # Eliminar filas con datos faltantes
    df = df.dropna()
    #limpieza principales caracteres y conversion a minusculas
    df=df.apply(lambda x: x.astype(str))
    df=df.apply(lambda x: x.str.replace(",", ""))
    df=df.apply(lambda x: x.str.replace("$", ""))
    df=df.apply(lambda x: x.str.replace("_", " "))
    df=df.apply(lambda x: x.str.replace("-", " "))
    df=df.apply(lambda x: x.str.lower())
    # Convertir la columna 'fecha_de_beneficio' al formato de fecha adecuado
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'], errors='coerce')
    # Limpiar los valores de la columna 'monto_del_credito'
    df['monto_del_credito'] = df['monto_del_credito'].astype(float)
    # Eliminar filas duplicadas
    df = df.drop_duplicates()
    return df


# Cargar el DataFrame desde el archivo CSV
file_path = 'solicitudes_credito.csv'
df = pd.read_csv(file_path, sep=';')
# Limpiar el DataFrame
df_cleaned = clean_data(df)
# Mostrar el DataFrame limpio
print(df_cleaned)
# Guardar el DataFrame limpio en un nuevo archivo CSV
df_cleaned.to_csv('datos_limpios.csv', index=False)

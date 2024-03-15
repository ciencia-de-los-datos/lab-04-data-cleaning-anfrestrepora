"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data(df):

    df = pd.read_csv("solicitudes_credito.csv", sep=";")
        # Eliminar filas con datos faltantes
    df = df.dropna()
    

    # Convertir la columna 'fecha_de_beneficio' al formato de fecha adecuado
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'], errors='coerce')

    # Limpiar los valores de la columna 'monto_del_credito'
    df['monto_del_credito'] = df['monto_del_credito'].str.replace('$', '').str.replace(',', '').astype(float)

    # Limpiar los valores de las columnas 'sexo', 'tipo_de_emprendimiento' y 'idea_negocio'
    df['sexo'] = df['sexo'].str.lower()
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.lower()
    df['idea_negocio'] = df['idea_negocio'].str.lower()

    # Asegurarse de que los valores de las columnas 'barrio', 'estrato', 'comuna_ciudadano' y 'línea_credito' sean adecuados
    df['barrio'] = df['barrio'].str.strip()
    df['estrato'] = pd.to_numeric(df['estrato'], errors='coerce')
    df['comuna_ciudadano'] = pd.to_numeric(df['comuna_ciudadano'], errors='coerce')
    df['línea_credito'] = df['línea_credito'].str.lower()

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

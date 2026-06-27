import pandas as pd
import mysql.connector 
from mysql.connector import  Error

## configuracion de la bases de datos
host= '127.0.0.1'
user= 'root'
password= ''
database = 'bd_etl'

def extract_data(file_path):
    print(f'Extrayendo data de {file_path}')
    data = pd.read_csv(file_path)
    print(data.head())
    return data

def transform_data(data):
    print('Transformando')
    data = data.dropna()
    data = data.drop_duplicates()
    data.columns = data.columns.str.lower()
    print(data.head())
    return data

def load_data(data, table_name): 
    try: 
        connection = mysql.connector.connect(
            host= host,
            user=user,
            password= password, 
            database = database
        )
        print('conexion exitosa')
    except Error as e:
        print(e)
    
    cursor = connection.cursor()
    #cursor.execute(f'create table if not exists {table_name}')
    cursor.close()


def proceso_etl():
    
    clientes = extract_data('data/clientes.csv')
    ventas = extract_data('data/ventas.csv')

    clientes_transformed = transform_data(clientes)
    ventas_transformed =  transform_data(ventas)
    
    load_data(clientes_transformed, 'clientes')
    load_data(ventas_transformed, 'ventas')

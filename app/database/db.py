import sqlite3

def get_db_connection():
    conn = sqlite3.connect('company.db')  # Nombre del archivo de la base de datos
    conn.row_factory = sqlite3.Row  # Permite acceder a las columnas por nombre
    return conn

def fetch_all_from_table(table_name):
    conn = get_db_connection()
    data = conn.execute(f'SELECT * FROM {table_name}').fetchall()  # Realiza la consulta
    conn.close()
    return [dict(row) for row in data]  # Devuelve los resultados como una lista de diccionarios

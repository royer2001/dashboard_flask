import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('company.db')
cursor = conn.cursor()

# Crear la tabla
cursor.execute('''
    CREATE TABLE IF NOT EXISTS empleados (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        edad INTEGER NOT NULL,
        ciudad TEXT NOT NULL,
        salario REAL NOT NULL
    )
''')

# Insertar 5 registros de ejemplo
empleados = [
    ('Juan Pérez', 28, 'Madrid', 30000.00),
    ('Ana García', 34, 'Barcelona', 35000.50),
    ('Luis Martínez', 45, 'Valencia', 40000.75),
    ('Sofía López', 29, 'Sevilla', 31000.25),
    ('Pedro Gómez', 39, 'Bilbao', 45000.00)
]

cursor.executemany('INSERT INTO empleados (nombre, edad, ciudad, salario) VALUES (?, ?, ?, ?)', empleados)

# Guardar (commit) los cambios y cerrar la conexión
conn.commit()
conn.close()

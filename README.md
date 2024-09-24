# DASHBOARD EN FLASK

Genera graficos usando Matplotlib y Flask

## Características

- Conexión a base de datos y consultas
- Generar gráficos con Matplotlib y Numpy

## Requisitos previos

Antes de comenzar, asegúrate de tener instalado:

- Python 3.7+
- pip (gestor de paquetes de Python)

## Instalación

1. Clona este repositorio:
   ```
   git clone https://github.com/royer2001/dashboard_flask.git
   ```

2. Cambia al directorio del proyecto:
   ```
   cd dashboard_flask
   ```

3. Crea un entorno virtual:
   ```
   python -m venv dash-env
   ```

4. Activa el entorno virtual:
   - En Windows:
     ```
     dash-env\Scripts\activate
     ```
   - En macOS y Linux:
     ```
     source dash-env/bin/activate
     ```

5. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

## Uso

1. En la carpeta app/database ejecuta el archivo connection.py desde la terminal para generar la base de datos en SQLite

2. Ejecuta la aplicación Flask:
   ```
   python app.py
   ```

3. Abre tu navegador y visita `http://localhost:5000`.

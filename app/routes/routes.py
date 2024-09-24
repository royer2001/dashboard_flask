from flask import Blueprint, render_template, jsonify
from app.services.graficos import generar_grafico_barras, generar_grafico_pie
from app.database.db import fetch_all_from_table

# Crear un blueprint para las rutas
main = Blueprint('main', __name__)

@main.route('/')
def index():
    table_name = 'empleados'  # Nombre de la tabla
    data = fetch_all_from_table(table_name)

    edades = []
    salarios = []
    cantidad_personas = {}

    for empleado in data:
        edades.append(empleado['edad'])
        salarios.append(empleado['salario'])
        ciudad = empleado['ciudad']

        # Contar cuántas personas hay por ciudad
        if ciudad in cantidad_personas:
            cantidad_personas[ciudad] += 1
        else:
            cantidad_personas[ciudad] = 1

    # Convertir el diccionario en listas para los gráficos
    ciudades_unicas = list(cantidad_personas.keys())
    cantidades = list(cantidad_personas.values())

    # Llamada a las funciones que generan los gráficos
    imagen_barras = generar_grafico_barras(edades, salarios)
    imagen_pie = generar_grafico_pie(ciudades_unicas, cantidades)

    return render_template('index.html', imagen_barras=imagen_barras, imagen_pie=imagen_pie)
